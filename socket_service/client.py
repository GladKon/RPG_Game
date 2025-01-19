import socket
import json
import time
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1', 8080))

end = time.time()
while True:
    start = time.time()
    if start - end >= 5:
        data = b'Hello, i am bot'
        client_socket.send(data)
        end = time.time()

        data = client_socket.recv(1024)
        print(f'Server data: {data.decode()}')


client_socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket1.connect(('127.0.0.2', 8080))


while True:
    start = time.time()
    if start - end >= 5:
        data = b'Hello, i am player'
        client_socket1.send(data)
        end = time.time()

        data = client_socket1.recv(1024)
        print(f'Server data: {data.decode()}')

client_socket2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket2.connect(('127.0.0.2', 12345))
data = [1234,56453,23521356]

client_socket2.send(json.dumps(data).encode('UTF-8'))

data = client_socket2.recv(1024)
print(f'Server data: {data.decode()}')

# client_socket.close()
# client_socket1.close()

