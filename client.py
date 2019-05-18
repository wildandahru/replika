#Di sini klien sebagai pengirim file
import socket, os, sys

ip = input("Masukkan IP : ")
port = 9999
ukuran = 0
lok = ''
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	#membuat blok try
try:
	#melakukan koneksi pada socket menggunakan ip dan port yg ada
	client.connect((ip, port))
except:
	print ("Tidak bisa melakukan binding ke IP")
	sys.exit(0)

#menerima file
	f = open(lok, 'w')
	data = server.recv(1024)
	while data :
		f.write((data).decode('latin-1'))
		data = server.recv(1024)
		if "STOP" in data:
			break
	f.close()
