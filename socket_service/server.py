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


def handle_server_message_from_client(client_socket, client_address):
    while True:
        message = client_socket.recv(1024)
        if not message:
            print(f"Клиент {client_address} отключился")
            break

        message = json.loads(message.decode("utf-8"))
        print(f'Сообщение от {client_address}: {message}')

def first_message(client_socket,lobies):

    message = client_socket.recv(1024)
    message = json.loads(message.decode("utf-8"))
    if message['CREATER']:
        lobbies[message['name_of_room']] = {'Status': 'Lobby', 'Admin': message['player_id'],
                                            'Players_list': [message['name']], 'Sockets_list': [client_socket]}
    else:
        lobbies[message['name_of_room']]['Players_list'].append(message['name'])
        lobbies[message['name_of_room']]['Sockets_list'].append(client_socket)
    return lobbies


def handle_client(client_socket, client_address):
    print(f"New connect:{client_address}")
    global lobbies
    print(lobbies)
    lobbies = first_message(client_socket, lobbies)
    print(lobbies)
    threading_client = threading.Thread(target=handle_server_message_from_client, args=(client_socket, client_address))
    threading_client.start()
    try:
        client_socket.sendall(b"Hello\n")
        while True:
            # message = client_socket.recv(1024)
            # if not message:
            #     print(f"Клиент {client_address} отключился")
            #     break
            # print(f'Сообщение от {client_address}: {message.decode("utf-8")}')
            # client_socket.sendall(f"You said: {message.decode('utf-8')}".encode('utf-8'))
            data = input()
            client_socket.sendall(data.encode('utf-8'))
    except ConnectionResetError:
        print(f'Клиент {client_address} принудительно закрыл соединение.')
    finally:
        client_socket.close()

lobbies = {}
def main():
    server_ip = '0.0.0.0'
    server_port = 8080
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
