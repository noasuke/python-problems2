import string
str = input()
lower = 0
upper = 0
# for i in str:
#   if ord(i) in range(ord('a'),ord('z')):
#     lower+=1
#   else:
#     upper+=1

# for c in str:
#   if c in string.ascii_lowercase:
#     lower+=1
#   else:
#     upper+=1

caps = 'abcdefghijklmnopqrstuwxyz'
for c in str:
  if c in caps:
    lower+=1
  else:
    upper+=1

print(f'{lower}')
print(f'{upper}')