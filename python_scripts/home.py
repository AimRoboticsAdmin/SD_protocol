# home.py

from common import send_command

def move_home():
    send_command('home')

if __name__ == '__main__':
    move_home()
