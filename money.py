st = input()
patterns = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.', ',']

isValid = True

for c in st:
  if c not in patterns:
    isValid = False
    break

if isValid:
  if st.count('.')>1:
    isValid = False
  elif st.count('.')==1:  
    temp = st.split('.')
    if len(temp[1])>2:      # invalid when more than 2 precision
      isValid = False
    else:
      tmp = temp[0].split(',')
      i = 0
      while i<len(tmp):

        if i==0:
          if len(tmp[i])>3:
            isValid = False
        else:
          if len(tmp[i])!=3:
            isValid = False
        i+=1
    tempo = ''
    if isValid:
      for c in tmp:
        tempo += c
      tempo = int(tempo)+1
      st = ''
      st = str(tempo) + '.' + temp[1]
  else:
    tmp = st.split(',')
    # print(tmp)
    i = 0
    while i<len(tmp):
      # print(tmp[i])
      if i==0:
        if len(tmp[i])>3:
          isValid = False
      else:
        if len(tmp[i])!=3:
          isValid = False
      i+=1
    
    st = ''
    if isValid:
      for c in tmp:
        st += c
      st = int(st)+1
      st = str(st)

  if isValid:
    print(st)
  else:
    print('ERROR')
else:
  print('ERROR')