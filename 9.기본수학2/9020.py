def prime(n):
    if n<2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

t=int(input())

for i in range(t):
    num=int(input())
    for j in range(num//2,1,-1):
        if prime(j) and prime(num-j):
            print(j,num-j)
            break