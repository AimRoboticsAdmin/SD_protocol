# stop.py

from common import send_command

def stop_movement():
    send_command('stop')

if __name__ == '__main__':
    stop_movement()
