# 2021/10/08

import sys


def dfs(x, y):
    # 주어진 범위를 벗어날 경우 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False

    #현재 노드를 아직 방문하지 않았다면
    if graph[x][y]==0:
        #해당 노드를 방문 처리 한다
        graph[x][y] == 1

        #상,하,좌,우 위치들도 모두 재귀적으로 호출한다.
        #재귀적으로 호출되는 dfs들은 return 값이 없어 방문 처리 목적으로만 사용됨
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True
    return False

n, m = map(int, sys.stdin.readline().split())

# 2차원 리스트의 앱 정보 입력 받기
graph = []
for i in range(n):
    graph.append(list(map(int, sys.stdin.readline())))

# 모든 노드(위치)에 대하여 음료수 채우기
result = 0
for i in range(n):
    for j in range(m):
        # 현재 위치에서 dfs를 수행한다
        # 방문 처리가 되었다면
        if dfs(i, j) == True:
            # 값을 하나 올려준다
            result += 1
print(result)
