num=int(input())

for i in range(1, num + 1):
    if num == i + sum(list(map(int, str(i)))): # 가장 작은 값부터 더한다, 그 더한 값이 num과 같을때 출력
        print(i)
        break

    if i == num:
        print(0)