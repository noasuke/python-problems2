str = input()

patterns = ['-', '.', '=', '$', '_']

if str.count('-')+str.count('.')+str.count('=')+str.count('$')+str.count('_') == 0:
  str = str.lower()

i = 0
s = ''
while i<len(str):
  if str[i] not in patterns:
    s += str[i]
  else:
    s += '|'
  i+=1

s = s.split('|')

i = 0
result = ''
while i<len(s):
  if i==0:
    result = s[i].lower()
  else:
    tmp = s[i].lower()
    result += tmp[0].upper() + tmp[1:]

  i+=1

print(result)