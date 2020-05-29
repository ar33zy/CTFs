a = [x.strip().split('  ') for x in open('test').readlines() if x.strip()]

flag = ''

counter = 0
b = [6,12,5,20,15,1,5,3,4,10,13,16,7,12,14,8]
for x in a:
    flag += x[b[counter]-1]
    counter += 1
print flag
