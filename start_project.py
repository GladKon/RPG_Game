import subprocess
subprocess.run(['python', 'socket_service/server.py'])
subprocess.run(['python', 'server_service/web_server/main.py'])
subprocess.run(['python', 'client_service/main.py'])



