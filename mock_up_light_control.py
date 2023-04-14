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

# send message
msg_initial = 'f5 fe'
msg_end = '00 ef'

msg_red = 'ff'   # light strength is from 00 to ff
msg_green = 'ff'
msg_blue = 'ff'

'''
#00 SEH
#01 Ross Hall
#02 Rome Hall
#03 Rice Hall
#04 Smith Hall of Art
#05 Milken Institute School of Public Health
#06 Phillips Hall
#07 GWU Hospital
#08 GW Medical Faculty Associates Ambulatory Care Center
#09 Student Center
#0a Fulbright Hall
#0b Munson Hall
#0c JBKO Hall
#0d District Hall
#0e Lafayette Hall
#0f Washington Cir NW
#10 Pennsylvania Avenue NW
#11 New Hampshire Avenue NW
#12 H St
#13 I St
#14 K St
#15 24th St
#16 23rd St
#17 22nd St
#18 21st St
#19 Embassy of Spain
#1a The Chancellor
#1b One Washington Circle Hotel
#1c Embassy of Tajikistan
#1d Winston House Apartments
#1e Department of Global Health
#1f Reit Management Research Inc
#20 GW Training Center
#21 2100 L Street
#22 GWU HOR Center
#23 IISS-Americas
#24 International Finance Corporation
#25 The Avenue
#26 President Condominium
#27 Foggy Bottom Metro Station
#28 Road Lights
'''
# msg_building = '00'
# msg = msg_initial + msg_building + msg_red + msg_green + msg_blue + msg_end
# # msg = 'f5 fe 00 ff 00 00 00 ef'
# msg_bytes = bytes.fromhex(msg)  # send encoding format is Hex
# _socket.sendall(msg_bytes)

# for general command
msg = 'GALLOFF'   # open all - KALLON, colse all - GALLOFF, reset - RESET
msg_bytes = msg.encode('utf-8')
_socket.sendall(msg_bytes)

# for LOOP control
# buildings = ['00', '01', '02', '03', '04', '05', '06']
# for apt in buildings:
#     msg = msg_initial + apt + msg_red + msg_green + msg_blue + msg_end
#     msg_bytes = bytes.fromhex(msg)  # send encoding format is Hex
#     _socket.sendall(msg_bytes)
#     time.sleep(5)

# close socket
_socket.close()
