from pwn import *

conn = remote('rev.tamuctf.com',8188)
print conn.recvline()
print conn.recvline()
conn.send("WattoSays\n")
print conn.recvline()
	
