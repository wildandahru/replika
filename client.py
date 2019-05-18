#Di sini server sebagai penerima
import socket, os, sys

ip = input("Masukkan IP : ")
port = 9999
ukuran = 0
path = ''
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	#membuat blok try
try:
	#melakukan koneksi pada socket menggunakan ip dan port yg ada
	server.bind((ip, port))
except:
	print ("Tidak bisa melakukan binding ke IP")
	sys.exit(0)
server.listen(1)
conn, addr = server.accept()
	
#mengirim file
list = os.listdir(path)
for i in list:
	hitung = os.path.getsize(i)
	ukuran += hitung
	f = open(i, 'r', encoding='latin-1', errors='surrogateescape')
	data = f.read(1024)
	conn.sendall((data).encode('latin-1))
	f.close()
conn.send(("STOP").encode("ascii"))
