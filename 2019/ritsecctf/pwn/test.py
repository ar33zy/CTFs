from pwn import *
import os
import commands


dirs = sorted(os.listdir('./999bottles'))
values = []
for x in dirs:
  x = './999bottles/' + x
  bp = commands.getstatusoutput("objdump -D %s | grep '38 c2' -B 1 | head -n 1 | awk '{print $10}' | cut -d, -f1"%x)[1]
  value = commands.getstatusoutput("objdump -D %s | grep %s | head -n 1 | awk '{print $10}' | cut -d, -f1 | sed 's/\$//g'"%(x,bp))[1]
  if value:
    values.append(chr(int(value,16)))

print(values)
