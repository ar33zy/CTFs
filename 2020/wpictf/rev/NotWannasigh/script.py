import random


f = open('flag-gif.EnCiPhErEd', 'rb').read()
keys = [x.strip() for x in open('keys.txt').readlines()]


output = ""
for x in range(len(f)):
    output += chr( ord(f[x]) ^ int(hex(int(keys[x]))[-2:],16) )

print output
