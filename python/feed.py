# feed.py

from common import send_command
import sys

def set_prefeed_steps(steps):
    command = f'feed {steps}'
    send_command(command)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python feed.py <steps>")
    else:
        set_prefeed_steps(sys.argv[1])
