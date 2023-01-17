import sys
from collections import deque

def bfs(graph, start, answer):
    queue=deque([start])
    while queue:
        v=queue.popleft()
        for w in graph[v]:
            if answer[w]==-1: #방문하지 않은 노드면 추가 및 거리 갱신
                answer[w]=answer[v]+1
                queue.append(w)

city, road, distance, start = map(int,sys.stdin.readline().split())
answer= [-1]*(city+1) #방문 여부 및 거리 저장 
answer[start]=0

#인접리스트
graph=[ [] for _ in range(city+1) ]
for _ in range(road):
    a,b = map(int,sys.stdin.readline().split())
    graph[a].append(b)

bfs(graph, start, answer)

if answer.count(distance):
    for i in range(1,city+1):
        if answer[i]==distance:
            print(i)
else:
    print("-1")
