n=int(input())

while n>=2:
    for i in range(2,n+1):
        if n%i==0:
            n=n//i
            break
    print(i)