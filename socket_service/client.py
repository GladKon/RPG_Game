import socket
import sys
import threading
import time
import json

#
#
# def handle_message_to_server(client_socket):
#     while True:
#         data = client_socket.recv(1024)
#         print(f'Server data: {data.decode()}')
#
#
# def main():
#     server_ip = '127.0.0.1'
#     server_port = 8080
#     client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     client_socket.connect((server_ip, server_port))
#     thread_socket = threading.Thread(target=handle_message_to_server, args=(client_socket, ))
#
#     try:
#
#         thread_socket.start()
#         while True:
#             print('Введите сообщение.')
#             data = input()
#             client_socket.send(data.encode('utf-8'))
#
#
#
#     except ConnectionRefusedError:
#         print(f"Не удалось подключится к серверу {server_ip}:{server_port}.")
#     except Exception as e:
#         print(f'Произошла ошибка {e}')
#     finally:
#         client_socket.close()
#         sys.exit()
# if __name__ == "__main__":
#     main()
#
#
# #
# #
# # client_socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# # client_socket1.connect(('127.0.0.2', 8080))
# #
# #
# # while True:
# #     start = time.time()
# #     if start - end >= 5:
# #         data = b'Hello, i am player'
# #         client_socket1.send(data)
# #         end = time.time()
# #
# #         data = client_socket1.recv(1024)
# #         print(f'Server data: {data.decode()}')
# #
# # client_socket2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# # client_socket2.connect(('127.0.0.2', 12345))
# # data = [1234,56453,23521356]
# #
# # client_socket2.send(json.dumps(data).encode('UTF-8'))
# #
# # data = client_socket2.recv(1024)
# # print(f'Server data: {data.decode()}')
#
# # client_socket.close()
# # client_socket1.close()
#

d = {"list": [1, 2, 3], "name": "Artem"}
letter = json.dumps(d).encode("utf-8")
l = len(letter)
print(f"{l:04d}")
