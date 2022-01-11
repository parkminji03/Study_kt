max_n=123456*2+1
check_list=[True for i in range(max_n)]

for i in range(2,int(max_n**0.5)+1):
    if check_list[i]==True:
        j=2
        while i*j <= max_n:
            check_list[i*j]=False
            j+=1

while True:
    cnt=0
    a=int(input())
    b=2*a
    if a==0:
        break
        
    for i in range(a+1,b+1):
        if check_list[i]:
            cnt+=1
    print(cnt)