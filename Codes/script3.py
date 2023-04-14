import socket
import time

# Encoding_format = 'utf-8'
HOST = '192.168.1.1'
PORT = 4031
BUF_SIZE = 1024
ADDR = (HOST, PORT)

# creat socket
_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # AF_INET is for IPV4, SOCK_STREAM is for TCP model
_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
_socket.connect(ADDR)
print('...connected from:', ADDR)

msg = 'GALLOFF'
msg_bytes = msg.encode('utf-8')
_socket.sendall(msg_bytes)
print("All OFF")
time.sleep(1)

msg = 'RESET'
msg_bytes = msg.encode('utf-8')
_socket.sendall(msg_bytes)
print("Reset")
time.sleep(1)

msg_initial = 'f5 fe '
msg_red = 'ff '  # light strength is from 00 to ff
msg_green = '00 '
msg_blue = '00 '
msg_end = '00 ef'
# for LOOP control
buildings = ['00','01']

for apt in buildings:
    msg = msg_initial + apt + msg_red + msg_green + msg_blue + msg_end
    msg_bytes = bytes.fromhex(msg)  # send encoding format is Hex
    _socket.sendall(msg_bytes)
    time.sleep(0.1)
    print("Light up:", apt)