#find 함수
#해당 문자의 위치를 알려줌, 찾는 문자열이 없으면 자동으로 -1 반환
s=input()
a='abcdefghijklmnopqrstuvwxyz'
for i in a:
    print(s.find(i),end=' ')