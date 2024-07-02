# retr.py

from common import send_command
import sys

def set_retraction_steps(steps):
    command = f'retr {steps}'
    send_command(command)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python retr.py <steps>")
    else:
        set_retraction_steps(sys.argv[1])
