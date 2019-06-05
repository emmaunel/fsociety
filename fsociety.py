import os
import time
import sys
import subprocess
from random import SystemRandom
from string import ascii_letters, digits, punctuation
from Crypto.Hash import SHA256
from Crypto.Cipher import AES
from Crypto import Random

SALT = 'fsociety'


def generate_key(salt):
    os.urandom(16)
    print('Loading Source of Entropy')
    password = salt.join((''.join(
        SystemRandom().choice(ascii_letters + digits + punctuation) for x in range(SystemRandom().randint(40, 160))))
                         for x in range(SystemRandom().randint(80, 120)))
    # print('password ', password)
    update(0.3)
    time.sleep(0.4)
    update(0.6)
    time.sleep(0.2)
    update(1)
    print()
    print('\nGenerating keys')
    update(0.3)
    hasher = SHA256.new(password.encode('utf-8'))
    # print("Hasher ", hasher)
    time.sleep(0.6)
    update(0.5)
    time.sleep(0.6)
    update(1)
    print()
    print()
    return hasher.digest()


def update(progress):
    barLenght = 23
    status = ""
    if isinstance(progress, int):
        progress = float(progress)
    if progress >= 1:
        progress = 1
        status = "COMPLETE"
    block = int(round(barLenght*progress))
    loading = "\r{0}\t\t{1}".format("#"*block + " " * (barLenght - block), status)
    sys.stdout.write(loading)
    sys.stdout.flush()

def main():
    subprocess.call('clear')
    print('Executing FuxSocy')
    key = generate_key(SALT)
    print("ket", key)


if __name__ == '__main__':
    main()
