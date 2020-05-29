from pwn import *

lines = open('output').readlines()

test = []
for x in lines:
    line = x.strip()
    test += [chr(ord(x)^0x42) for x in p64(int(line,16))]


test = ''.join(test)
print(test)
