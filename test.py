import socket

import time

HOST = "10.1.1.6"
PORT = 30002

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((HOST, PORT))
s.send(("set_digital_out(1,False)"+"\n").encode('utf8'))
s.send(("movej([0.1,0.1,0.1,0,3.14,0])"+"\n").encode('utf8'))