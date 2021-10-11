#상근이의 여행

#클래스 임포트
from queue import PriorityQueue

#우선순위 큐 생성
#que = PriorityQueue()

#특정 최대 크기 설정
que = PriorityQueue(maxsize=3)

#원소 추가
que.put(3)

#원소 삭제
que.get(3)