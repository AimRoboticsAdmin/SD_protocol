# tbps.py

from common import send_command
import sys

def set_toolbar_speed(speed):
    if speed >=0 and speed <=100:
        command = f'tbps {speed}'
        send_command(command)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python tbps.py <speed>")
    else:
        set_toolbar_speed(sys.argv[1])
