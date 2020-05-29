import random
from hashlib import sha256

def proof():
    strings = "abcdefghijklmnopqrstuvwxyzWOERFJASKL"
    prefix = "".join(random.sample(strings, 6))
    s = ''
    for i in range(4):
        s += random.choice(strings)
    starwith = sha256((prefix+s).encode()).hexdigest()[:6]
    pf = """
sha256("%s"+str).hexdigest().startswith("%s") == True
Please give me str of length 3
"""%(prefix, starwith)
    print(pf)
    s = input().strip()
    if sha256((prefix+s).encode()).hexdigest().startswith(starwith):
        exit(0)
    else:
        exit(1)

proof()
