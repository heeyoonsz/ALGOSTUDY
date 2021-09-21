# 블랙잭
N,M= map(int,input().split()) # 숫자 개수 n과 최대합 m
card=list(map(int,input().split(' '))) #그 다음 n의 숫자를 받고 ' '로 떼서 리스트에 넣는다.
card.sort() # 오름차순 정렬
sum=0
result=0
for i in range(0,N):
    for j in range(1,N):
        for k in range(2, N):
            sum=card[i]+card[j]+card[k]
            if sum>M:
                break
            elif sum<=M:
                result=max(result,sum)
print(result)