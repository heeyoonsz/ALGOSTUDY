#거북이

a,b,c,d = map(int,input().split())
l = [a,b,c,d]

# sort 없이 정렬 연습
for i in range(len(l)): #리스트 l의 길이동안 반복
    s = len(l) - i
    for j in range(1, s):
        if l[j-1] >= l[j]:
            temp = l[j-1]
            l[j-1] = l[j]
            l[j] = temp
#print(l)

print(l[0]*l[2])