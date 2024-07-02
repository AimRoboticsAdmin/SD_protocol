# size.py

from common import send_command
import sys

def set_syringe_size(size):
    command = f'size {size}'
    send_command(command)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python size.py <size>")
    else:
        set_syringe_size(sys.argv[1])
