from xml.dom import minidom
import binascii
import os


while True:

  os.system('wget https://challenges.neverlanctf.com:1150/svg.php -O svg.php')

  doc = minidom.parse('svg.php')  # parseString also exists
  path_strings = [str(path.getAttribute('style')) for path
                in doc.getElementsByTagName('rect')]

  flag = ''
  for x in path_strings:
    if x == 'fill:#00ff00':
        flag += '0'
    else:
        flag += '1'

  flag = [flag[i:i+8] for i in range(0, len(flag), 8)]

  flagger = ''
  for x in flag:
    n = int('0b{}'.format(x), 2)
    flagger += binascii.unhexlify('%x' % n)
  
  outfile = open('output','a')
  outfile.write(flagger + '\n')
  print flagger
