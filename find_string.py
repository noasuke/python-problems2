str1 = input()
str2 = input()
str3 = input()

print(f'{str1.find(str2)}')
print(f'{str1.count(str2)}')

str1=str1.replace(str2, str3)
print(f'{str1}')
