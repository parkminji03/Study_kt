a=int(input())

for i in range(a):
    n,s=input().split()
    p=""
    for j in s:
        p+=j*int(n)
    print(p)