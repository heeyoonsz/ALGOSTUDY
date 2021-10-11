# 유기농 배추

import sys

#상하좌우
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]

T = int(sys.stdin.readline())

for _ in range(T):
    # 가로, 세로, 배추 개수
    M, N, K = map(int, input().split())

    # 열과 행 개수
    result = [[0] * M for _ in range(N)]

    # 배추의 위치
    for _ in range(K):
        x, y = map(int, input().split())

        result[y][x] = 1

    cnt = 0

    for i in range(N):
        for j in range(M):
            #값이 1인 노드 방문시
            if result[i][j] == 1:
                cnt += 1
                #방문한 노드의 값은 0으로 업데이트
                result[i][j] = 0
                #상하좌우
                sub = [[i - 1, j], [i + 1, j], [i, j - 1], [i, j + 1]]

                while sub:
                    x, y = sub.pop()
                    if -1 < x < N and -1 < y < M:
                        #값이 1인 노드 방문 시 방문한 노드의 값을 0으로 업데이트
                        if result[x][y] == 1:
                            result[x][y] = 0
                            sub.append([x, y - 1])
                            sub.append([x, y + 1])
                            sub.append([x - 1, y])
                            sub.append([x + 1, y])
    print(cnt)
