str = input()

patterns = ['-', '.', '=', '$', '_']

# if str[0] not in patterns:
str = str.replace(str[0], str[0].lower())

i = 1
while i<len(str):
  if str[i] in patterns:
    s = str[i+1].upper()
    str = str[0:i] + s + str[i+2:]
  i+=1

print(str)