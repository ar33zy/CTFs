#!/usr/bin/python3

def xor(s1,s2):
    return ''.join(chr(ord(a) ^ ord(b)) for a, b in zip(s1, s2))

def encrypt(a):
    some_text = a[::2]

    randnum = 14
    text_length = len(some_text)
    endtext = ""
    for i in range(1, text_length + 1):
      weirdtext = some_text[i - 1]
      if weirdtext >= "a" and weirdtext <= "z":
          weirdtext = chr(ord(weirdtext) + randnum)
          if weirdtext > "z":
              weirdtext = chr(ord(weirdtext) - 26)
      endtext += weirdtext
    randtext = a[1::2]

    xored = xor("aaaaaaaaaaaaaaa", randtext)
    hex_xored = xored.encode("utf-8").hex()

    return endtext + hex_xored

def decrypt(msg):
    div = int(len(msg)/3)
    part1 = msg[:div]
    part2 = bytes.fromhex(msg[div:]).decode('utf-8')
    part2 = xor("a"*div, part2)
    temp_part1 = ""
    chars = 'abcdefghijklmnopqrstuvwxyz'

    for i in range(1, len(part1) + 1):
      weirdtext = part1[i - 1]
      if weirdtext >= "a" and weirdtext <= "z":
        weirdtext = chr(ord(weirdtext) - 14)
        if weirdtext < "a":
          weirdtext = chr(ord(weirdtext) + 26)
      temp_part1 += weirdtext

    flag = ""
    for i in range(len(part2)):
        flag += temp_part1[i]
        flag += part2[i]
    print(flag)


def main():
    decrypt('fqtbjfub4uj_0_d00151a52523e510f3e50521814141c')

if __name__ == "__main__":
    main()
