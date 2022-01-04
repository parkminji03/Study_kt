import math

def sum_n(n):
    sum=0
    for i in range(1,n+1):
        sum+=i
    return sum

x=int(input())
i=math.floor(math.sqrt(x))
while x>sum_n(i):
    i+=1
a=x-sum_n(i-1)
b=i+1-a

if i%2==0:
    print(a,"/",b,sep='')
else:
    print(b,"/",a,sep='')