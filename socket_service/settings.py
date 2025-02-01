import os
import dotenv

dotenv.load_dotenv()

SERVER_IP = os.getenv('SERVER_IP')
SERVER_PORT = int(os.getenv('SERVER_PORT'))
