a=input().lower()
arr=['abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
result=0
for x in a:
    for i in range(len(arr)):
        if x in arr[i]:
            result+=i+3

print(result)