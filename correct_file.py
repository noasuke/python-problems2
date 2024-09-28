str = input()
patterns = ['\\', '/', '*', ':', '|', '"', '<', '>', ' ']

count_dot = str.count('.')
if count_dot == 0:
  i = 0
  while i<len(str):
    if str[i] in patterns:
      str = str.replace(str[i], '_')
    
    i+=1
  if len(str)>15:
    str = str[:15]

elif count_dot == 1:
  i = 0
  while i<len(str):
    if str[i] in patterns:
      str = str.replace(str[i], '_')
    
    i+=1
  
  tmp = str.split('.')
  str = ''
  if len(tmp[0])>15:
    str += tmp[0][:15] + '.'
  else:
    str += tmp[0] + '.'
  
  if len(tmp[1])>3:
    str += tmp[1][:3]
  else:
    str += tmp[1]

else:
  i = 0
  while i<len(str):
    if str[i] in patterns:
      str = str.replace(str[i], '_')
    
    i+=1

  tmp = str.split('.')
  # print(tmp)
  str = ''
  i = 0
  while i<count_dot-1:
    str += tmp[i] + '_'
    i+=1
  str += tmp[i]

  if len(str)>15:
    str = str[:15]

  if len(tmp[i+1])>3:
    tmp[i+1] = tmp[i+1][:3]

  str += '.' + tmp[i+1]

print(str)



