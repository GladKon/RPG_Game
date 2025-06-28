import json
import os
import socket
import threading

SERVER_IP=welcoming-truth.railway.app
SERVER_PORT=int(os.getenv('PORT',8081))


def first_message(client_socket, message) -> None:
    """Функция, которая обрабатывает первое сообщение.

    :param client_socket: Объект сокета, по которому будут передаваться сообщения;
    :param message: Первое сообщение от конкретного клиента, которое принял сервер;
    """
    if message['CREATER']:
        lobbies[message['name_of_room']] = {'Status': 'Lobby', 'Admin': message['player_id'],
                                            'players_list': [message['name']], 'Sockets_list': [client_socket]}
        data = lobbies[message['name_of_room']]['players_list']
        final_message = {'type_of_message': "first_message_admin", "content": data}
        client_socket.send(json.dumps(final_message).encode('utf-8'))

    else:
        lobbies[message['name_of_room']]['players_list'].append(message['name'])
        lobbies[message['name_of_room']]['Sockets_list'].append(client_socket)
        data = lobbies[message['name_of_room']]['players_list']
        final_message = {"type_of_message": "first_message_not_admin", "content": data}
        for client in lobbies[message['name_of_room']]['Sockets_list']:
            client.send(json.dumps(final_message).encode('utf-8'))

def start_lobby(content):
    Players_coords = {}
    for player in content['players_list']:
        Players_coords[player] = [100, 100]
    data = {'Status': content['Status'], 'Time_start': content['Time_start'],
            'Players_coords': Players_coords}
    final_message = {"type_of_message": "start_game", "content": data}
    for client in lobbies[content['name_of_room']]['Sockets_list']:
        client.send(json.dumps(final_message).encode('utf-8'))
    lobbies[content['name_of_room']]['Status'] = 'Running'

def running_game(content,client_socket):
    final_message = {"type_of_message": "coords", "content": content}
    for client in lobbies[content['name_of_room']]['Sockets_list']:
        if client != client_socket:
            client.send(json.dumps(final_message).encode('utf-8'))

def handle_client(client_socket, client_address):
    print(f"New connect: {client_address}")
    try:
        while True:
            len_message = int(client_socket.recv(4).decode('utf-8'))
            message = json.loads(client_socket.recv(len_message).decode('utf-8'))
            type_message = message['type_message']
            content = message['content']
            match type_message:
                case 'first_message':
                    first_message_thread = threading.Thread(target=first_message, args=(client_socket, content))
                    first_message_thread.start()
                case 'start_lobby':
                    start_lobby(content)
                case 'running_game':
                    running_game(content, client_socket)
    except ConnectionResetError:
        print(f'Клиент {client_address} принудительно закрыл соединение.')
    finally:
        client_socket.close()


lobbies = {}


def main():
    server_ip = SERVER_IP
    server_port = SERVER_PORT
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
    server_socket.bind((server_ip, server_port))
    server_socket.listen(5)

    print(f'Server started!')

    while True:
        client_socket, client_address = server_socket.accept()
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_thread.start()


if __name__ == '__main__':
    main()
