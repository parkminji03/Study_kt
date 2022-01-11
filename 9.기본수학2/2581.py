m=int(input())
n=int(input())
list1=[]
list2=[]

for i in range(m,n+1):
    list1.append(i)

for i in list1:
    cnt=0
    if i!=1:
        for j in range(2,i):
            if i%j==0:
                cnt=1
                break
        if cnt==0:
            list2.append(i)

if len(list2):
    print(sum(list2))
    print(min(list2))
else:
    print(-1)