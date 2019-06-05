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
    print('password ', password)
    # update progress
    time.sleep(0.4)
    # update progress
    time.sleep(0.2)
    # update again
    print()
    print('\nGenerating keys')
    # update
    hasher = SHA256.new(password.encode('utf-8'))
    print("Hasher ", hasher)
    time.sleep(0.6)
    # update
    time.sleep(0.6)
    # update
    print()
    print()
    return hasher.digest()


def main():
    subprocess.call('clear')
    print('Executing FuxSocy')
    key = generate_key(SALT)
    print("ket", key)


if __name__ == '__main__':
    main()
