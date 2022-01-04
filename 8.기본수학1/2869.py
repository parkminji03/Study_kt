a,b,v=input().split()
a= int(a)
b=int(b)
v=int(v)

n=(v-a)/(a-b)+1
if (v-a)%(a-b)==0:
    print(int(n))
else:
    print(int(n)+1)