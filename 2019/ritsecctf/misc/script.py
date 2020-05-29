from base64 import b32decode, b16decode, b64decode

orig = open('onionlayerencoding.txt').read()

a = b64decode(orig)
a = b16decode(a)
a = a.decode('hex')
a = b64decode(a)

print(len(set(a)))
