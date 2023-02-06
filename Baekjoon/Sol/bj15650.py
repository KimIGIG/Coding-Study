'''
1. 1부터 N까지 자연수 중 중복 없이 M개를 고른 수열
2. 오름차순
'''

from itertools import combinations

N, M = list(map(int, input().split()))

num = [x for x in range(1, N+1)]

'''
for case in combinations(num, M):
    print(*case)
'''

#nums = [0 for x in range(1, N+1)]
s = []

def dfs(depth):

    if len(s) == M:
        print(' '.join(map(str, s)))
        return

    for i in range(depth, N+1):
        if i not in s:
            s.append(i)
            dfs(i+1)
            s.pop()

dfs(1)