a,b,c=input().split()
a=int(a)
b=int(b)
c=int(c)

if b >= c:
    print(-1)
else:
    n=a//(c-b)
    print(n+1)