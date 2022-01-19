n=int(input())
p_list=[]

for i in range(n):
    w,h=map(int,input().split())
    p_list.append([w,h])
    
for i in p_list:
    grade=1
    for j in p_list:
        if i[0] < j[0] and i[1] < j[1]:
            grade+=1
    print(grade)