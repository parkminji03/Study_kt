n=int(input())
check=0

for i in range(n):
    set_list=[0,0,0,0,0,0,0]
    for j in range(len(str(i))):
        set_list[j]=int(str(i)[j])
    if i+sum(set_list)==n:
        print(i)
        check=1
        break

if check==0:
    print(0)