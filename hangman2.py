str = input()
length = len(str)
guess = []
while True:
  ch = input()
  if ch == '0':
    break
  else:
    guess.append(ch)

counter = 0
for c in str:
  if c not in guess and c != '-':
    str = str.replace(c, '-')

print(f'{str}')