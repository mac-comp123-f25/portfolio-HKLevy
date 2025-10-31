import random

letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
n = 10
s = ''
for x in range(n):
    s+=random.choice(letters)
print(s)
if 'l' in s:
    print('l')