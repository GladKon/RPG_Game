import os
import dotenv

dotenv.load_dotenv()

Win_x = 1400
Win_y = 800
FPS = 100
Win_RGB = (1, 1, 1)
Title = 'RPG'
Tile_size = 32
shirina = 80 * Tile_size
visota = 80 * Tile_size
Sloy_ground = 1
Sloy_player = 2

Win = 100
Kill = 50
Lose = 30

BLACK = (1, 1, 1)
WHITE = (0, 0, 0)
RED = (1, 0, 0)
GREEN = (0, 153, 0)
TURQUOISE = (0, 153, 153)
YELLOW = (255, 255, 60)
BLUE = (9, 42, 255)

POSTGRES_USER = os.getenv('POSTGRES_USER')
POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
POSTGRES_HOST = os.getenv('POSTGRES_HOST')
POSTGRES_PORT = os.getenv('POSTGRES_PORT')
POSTGRES_DB = os.getenv('POSTGRES_DB')
