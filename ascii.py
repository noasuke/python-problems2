data = []
while True:
  str = input()
  if str != '':
    data.append(str)
  else:
    break

result = ''
i = 0
while i<len(data):
  if i%2==0:
    result+=max(data[i])
  else:
    result+=min(data[i])
  i+=1

print(f'{result}')