# ping.py

from common import send_command

def check_connection():
    send_command('ping')

if __name__ == '__main__':
    check_connection()
