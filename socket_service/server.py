# import socket
# import _thread
#
# server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server_socket.bind(('0.0.0.0', 12345))
# server_socket.listen(1)
# print('Server started')
#
#
# def client_thread(client_socket):
#     data = client_socket.recv(1024)
#     data = data.decode('UTF-8')
#
#     print(f'Client send data: {data}')
#
#     client_socket.send(b'Data recieved')
#     client_socket.close()
# while True:
#     client_socket, client_adress = server_socket.accept()
#     print(f'Client accepted: {client_adress}')
#     _thread.start_new_thread(client_thread, (client_socket,))
import json

import socket
import threading
from plistlib import loads

from settings import SERVER_IP, SERVER_PORT


def handle_server_message_from_client(client_socket, client_address):
    room = ''

    while True:
        message = client_socket.recv(1024)
        if not message:
            print(f"Клиент {client_address} отключился")
            break

        message = message.decode("utf-8")
        print(message.split('\n'))
        if '\n' not in message:
            message = json.loads(message)
        print(message)
        if message.get('CREATER', False):
            room = message['name_of_room']

            lobbies[message['name_of_room']]['Status'] = message['Status']
            lobbies[message['name_of_room']]['Time_start'] = message['Time_start']

        else:

            message = message.split('\n')[-2]
            message = message.encode('utf-8')
            for oponnent in lobbies[room]['Sockets_list']:
                if oponnent != client_socket:
                    oponnent.sendall(message)

        print(lobbies)
        # if type(message) != dict:
        #     print(f'Сообщение от {client_address}: {message}')

def first_message(client_socket,message):

    # message = client_socket.recv(1024)
    # message = json.loads(message.decode("utf-8"))
    # room = message['name_of_room']
    # print(message)
    if message['CREATER']:
        lobbies[message['name_of_room']] = {'Status': 'Lobby', 'Admin': message['player_id'],
                                            'Players_list': [message['name']], 'Sockets_list': [client_socket]}
        data = lobbies[message['name_of_room']]['Players_list']

        client_socket.send(json.dumps(data).encode('utf-8'))

    else:
        lobbies[message['name_of_room']]['Players_list'].append(message['name'])
        lobbies[message['name_of_room']]['Sockets_list'].append(client_socket)
        data = lobbies[message['name_of_room']]['Players_list']
        for client in lobbies[message['name_of_room']]['Sockets_list']:

            client.send(json.dumps(data).encode('utf-8'))



def handle_client(client_socket, client_address):
    print(f"New connect:{client_address}")
    global lobbies

    try:
        while True:
            len_message = int(client_socket.recv(4).decode('utf-8'))
            message = json.loads(client_socket.recv(len_message).decode('utf-8'))
            type_message = message['type_message']
            content = message['content']

            # print(lobbies)
            if type_message == 'first_message':
                first_message_thread = threading.Thread(target=first_message, args=(client_socket,content))
                first_message_thread.start()
            elif type_message == 'start_lobby':

                print('Open the door')
                Players_coords = {}
                for player in content['Players_list']:
                    Players_coords[player] = [100, 100]
                data = {'Status': content['Status'], 'Time_start': content['Time_start'],
                        'Players_coords': Players_coords}
                for client in lobbies[content['name_of_room']]['Sockets_list']:
                    client.send(json.dumps(data).encode('utf-8'))

                # print(lobbies)
                lobbies[content['name_of_room']]['Status'] = 'Running'
            elif type_message == 'running_game':


                print(content)
                for client in lobbies[content['name_of_room']]['Sockets_list']:
                    if client != client_socket:
                        client.send(json.dumps(content).encode('utf-8'))





    except ConnectionResetError:
        print(f'Клиент {client_address} принудительно закрыл соединение.')
    finally:
        client_socket.close()

lobbies = {}
def main():
    server_ip = SERVER_IP
    server_port = SERVER_PORT
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((server_ip, server_port))
    server_socket.listen(5)

    print(f'Server started!')

    while True:
        client_socket, client_address = server_socket.accept()
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_thread.start()


if __name__ == '__main__':
    main()
