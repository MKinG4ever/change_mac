import os
import sys
import random
import time

timestamp = time.time()
rnd = random.random
now = time.ctime
dly = time.sleep
cmd = os.system
pen = os.popen


def main():
    try:
        print('Operation System: ')
        run(sys.argv[1])
    except Exception as err:
        print(str(err), '\n')
        answer = input('Please enter Device name (ex: wlan0) > ')
        for ch in f'Device selected: {answer}\n':
            print(ch, end='')
            dly(rnd() / 3.14)
        run(answer)


def run(device):
    cmd('sudo uname')  # get access
    print('\n> ifconfig\n')  # whitespace / Line
    cmd('ifconfig')  # show devices
    cmd(f'sudo ifconfig {device} down')  # try to get down device
    print(f'try to offline device {device}')
    cmd(f'echo "Device {device} is offline..."')
    print('\n> ifconfig\n')  # whitespace / Line
    cmd('ifconfig')  # show devices
    cmd(f'sudo ifconfig {device} down')  # try to get down device again
    print(f'try to change {device} MAC address.\n')
    cmd(f'sudo macchanger -r {device}')  # change mac by random
    cmd(f'sudo macchanger -a {device}')  # change mac as a NEW brand
    cmd(f'sudo ifconfig {device} up')  # get back device online
    print(f'\nDevice mac is changed, try to get device online again.')
    cmd(f'echo "Device {device} is online...\n"')
    print('> ifconfig\n')  # whitespace / Line
    cmd('ifconfig')  # show devices
    _char = ''
    for ch in 'Done! (Wrote by NightFox).':
        _char += ch
        print(f'\r{_char}', end='')
        dly(rnd() / 3.14)


if __name__ == '__main__':
    main()
