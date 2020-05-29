a = ''.join([x.decode('hex')[::-1] for x in ['1e5d75590d5e1946','5a5f755e1b754758','53454875']])
print ''.join([chr(ord(x)^42) for x in a])
