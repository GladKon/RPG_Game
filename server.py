import socket
import threading
import json

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(("127.0.0.1", 19450))
users = []
server.listen()


def handel_client(client):
    while True:
        try:
            data = client.recv(1024)
            data = json.loads(data.decode('utf-8'))

            data = json.dumps(data).encode('utf-8')
            for soct in users:
                if soct != client:
                    soct.send(data)
        except ConnectionResetError:
            print('Конец соединения!')
            users.remove(client)
            client.close()
            break


while True:
    client, a = server.accept()
    number = str(len(users)).encode('utf-8')
    users.append(client)
    client.send(number)
    treading = threading.Thread(target=handel_client, args=(client,))
    treading.start()