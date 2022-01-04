a=input()
alpha=['c=','c-','dz=','d-','lj','nj','s=','z=']

for i in alpha:
    if i in a:
        a=a.replace(i,'.')
print(len(a))