import time
import sys

def loading(n):
    for i in range(n):
        length = len('\rloading *****')+5
        sys.stdout.write('\rloading *'.ljust(length, ' '))
        time.sleep(0.15)
        sys.stdout.write('\rloading **'.ljust(length, ' '))
        time.sleep(0.15)
        sys.stdout.write('\rloading ***'.ljust(length, ' '))
        time.sleep(0.15)
        sys.stdout.write('\rloading ****'.ljust(length, ' '))
        time.sleep(0.15)
        sys.stdout.write('\rloading *****'.ljust(length, ' '))
        time.sleep(0.15)
        sys.stdout.write('\rloading ****'.ljust(length, ' '))
        time.sleep(0.15)
        sys.stdout.write('\rloading ***'.ljust(length, ' '))
        time.sleep(0.15)
        sys.stdout.write('\rloading **'.ljust(length, ' '))
        time.sleep(0.15)
        sys.stdout.write('\rloading *'.ljust(length, ' '))
        time.sleep(0.15)
    sys.stdout.write('\rDone!     \n')
