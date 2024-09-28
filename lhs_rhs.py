data = []
while True:
  str = input()
  if str != '-1':
    data.append(str.strip())
  else:
    break

result = []
for s in data:
  s = s.split('=', maxsplit=1)
  for idx, d in enumerate(s):
    s[idx] = d.strip()
  result.append(s)

max_length = 0
for r in result:
  if max_length<=len(r[0]):
    max_length = len(r[0])

for r in result:
  show = ''
  if len(r[0])!=max_length:
    length = len(r[0])
    for i in range(max_length-length):
      show += ' '
   
  show += r[0] + ' = ' + r[1]
  print(f'{show}')
  