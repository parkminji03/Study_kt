word=input().lower()
wordl=list(set(word))

cnt = []

for i in wordl:
    count=word.count(i)
    cnt.append(count)
if cnt.count(max(cnt))>=2:
    print("?")
else :
    print(wordl[(cnt.index(max(cnt)))].upper())