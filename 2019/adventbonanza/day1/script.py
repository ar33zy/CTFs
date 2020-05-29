import csv 
from itertools import groupby

keypad_keys = {
'N7110_KEYPAD_ZERO': '0',
'N7110_KEYPAD_ONE': '1',
'N7110_KEYPAD_TWO': '2',
'N7110_KEYPAD_THREE': '3',
'N7110_KEYPAD_FOUR': '4',
'N7110_KEYPAD_FIVE': '5',
'N7110_KEYPAD_SIX': '6',
'N7110_KEYPAD_SEVEN': '7',
'N7110_KEYPAD_EIGHT': '8',
'N7110_KEYPAD_NINE': '9',
'N7110_KEYPAD_STAR': '10',
'N7110_KEYPAD_HASH': '11',
'N7110_KEYPAD_MENU_LEFT': '100',
'N7110_KEYPAD_MENU_RIGHT': '101',
'N7110_KEYPAD_MENU_UP': '102',
'N7110_KEYPAD_MENU_DOWN': '103',
}

keypad_keys = {
'0': 'N7110_KEYPAD_ZERO',
'1': 'N7110_KEYPAD_ONE',
'2': 'N7110_KEYPAD_TWO',
'3': 'N7110_KEYPAD_THREE',
'4': 'N7110_KEYPAD_FOUR',
'5': 'N7110_KEYPAD_FIVE',
'6': 'N7110_KEYPAD_SIX',
'7': 'N7110_KEYPAD_SEVEN',
'8': 'N7110_KEYPAD_EIGHT',
'9': 'N7110_KEYPAD_NINE',
'10': 'N7110_KEYPAD_STAR',
'11': 'N7110_KEYPAD_HASH',
'100': 'N7110_KEYPAD_MENU_LEFT',
'101': 'N7110_KEYPAD_MENU_RIGHT',
'102': 'N7110_KEYPAD_MENU_UP',
'103': 'N7110_KEYPAD_MENU_DOWN'
}

ime_methods = {
'N7110_IME_T9': '0',
'N7110_IME_T9_CAPS': '1',
'N7110_IME_ABC': '2',
'N7110_IME_ABC_CAPS': '3'
}

chars = {
'N7110_KEYPAD_ZERO_ABC_CHARS': " 0",
'N7110_KEYPAD_ONE_ABC_CHARS': ".,'?!\"1-()@/:",
'N7110_KEYPAD_TWO_ABC_CHARS': "abc2",
'N7110_KEYPAD_THREE_ABC_CHARS': "def3",
'N7110_KEYPAD_FOUR_ABC_CHARS': "ghi4",
'N7110_KEYPAD_FIVE_ABC_CHARS': "jkl5",
'N7110_KEYPAD_SIX_ABC_CHARS': "mno6",
'N7110_KEYPAD_SEVEN_ABC_CHARS': "pqrs7",
'N7110_KEYPAD_EIGHT_ABC_CHARS': "tuv8",
'N7110_KEYPAD_NINE_ABC_CHARS': "wxyz9",
'N7110_KEYPAD_STAR_ABC_CHARS': "@/:_;+&%*[]{}",
'N7110_KEYPAD_HASH_CHARS': ime_methods }

presses = []
prev = 0
prev_key = ''
with open('sms3.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        if prev_key == row[1] and abs(int(row[0])-prev) > 1000 and not prev < 1:
          presses.append('|')
        presses.append(row[1])
        prev = int(row[0])
        prev_key = row[1]

print('-'.join(presses))
groups = groupby(presses)
result = [(label, sum(1 for _ in group)) for label, group in groups]

arrow_keys = ['100','101','102','103','|']
#print([r[0] for r in result if r[0] not in arrow_keys])

flag = []
flag2 = ['X']*1000
pos = 0
for i in result:
    k, v = i
    if (k == '100') and pos > 0:
        pos += (1*v)
        continue
    if k == '101':
        pos -= (1*v)
        continue
    if k in arrow_keys:
        continue

    if 'HASH' in keypad_keys[k]:
      continue
    else:
      getchars = chars[keypad_keys[k]+"_ABC_CHARS"]
      newchar = getchars[(v%len(getchars))-1]
      flag.insert(pos,newchar)
      flag2[pos] = newchar
      pos += 1

print(''.join(flag))
print(''.join(flag2))

# AOTW{l3ts_dr1nk_s0m3_eggn0g_y0u_cr4zy_d33r}
