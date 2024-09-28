str = input()
patterns = [',']

data = []
i = 0
start = 0

while i<len(str):
  if str[i] in patterns:
    data.append(str[start:i])
    start=i+1
  i+=1

data.append(str[start:i])
# print(data)

result = ''
size = len(data)
round = 0
for str in data:
  round += 1
  i = 0
  while i<len(str):
    if str[i] == ' ':
      str = str[i+1:]
      continue
    else:
      break

  count = 0
  i = len(str)-1
  
  while i>0:
    if str[i] == ' ':
      
      count+=1
    else:
      break
    i-=1

  str = str[:len(str)-count]
  if round != size:
    result += '"' + str + '"' + ","
  else:
    result += '"' + str + '"'
  # print(len(str))

print(result)