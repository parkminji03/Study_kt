n=int(input())
a=[]
if n==0:
    a.append(0)
    print(a[n])
elif n==1:
    a.append(0)
    a.append(1)
    print(a[n])
else:
    a.append(0)
    a.append(1)
    for i in range(2,n+1):
        r=a[i-2]+a[i-1]
        a.append(r)

    print(a[n])