from PIL import Image
import numpy as np

f = open("site_colors").read().split('\n\n')

l = [x.split('\n') for x in f]

def hex_to_rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i+lv//3], 16) for i in range(0, lv, lv//3))


final = []
for x in l:
    if x == ['']:
        continue
    col = [] 
    for y in x:
        if not y:
            continue
        y = y.replace('0x','#')
        col.append(hex_to_rgb(y))
    final.append(col)

array = np.array(final, dtype=np.uint8)
new_image = Image.fromarray(array)
new_image.save('new.png')
