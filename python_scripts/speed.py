# speed.py

from common import send_command
import sys

def set_dispensing_speed(speed):
    command = f'speed {speed}'
    send_command(command)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python speed.py <speed>")
    else:
        set_dispensing_speed(sys.argv[1])

