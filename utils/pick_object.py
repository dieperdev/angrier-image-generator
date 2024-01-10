import os
import random
import json

os.system('cls' if os.name == 'nt' else 'clear')

config_file = open('config.json', 'r')
config_data = config_file.read()
config_file.close()

config = json.loads(config_data)

def pick_random() -> str:
    return config['items'][random.randint(0, (len(config['items']) - 1))]