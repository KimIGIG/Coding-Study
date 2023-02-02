# 로또

import sys
from itertools import permutations # 순열 : 순서중요 -> 다 뽑아버린다.
from itertools import combinations # 조합 : 순서 중요하지 않기에 중복되는 것 제외하고 뽑는다.

input = sys.stdin.readline

def dfs(start, depth):
    if depth == 6:
        for i in range(6):
            print(combi[i], end=' ')
        print()
        return
    for i in range(start, len(s)):
        combi[depth] = s[i]
        dfs(i + 1, depth + 1)

combi = [0 for i in range(13)]

while True:
    
    # k = num[0] 의미 (6 < k 13)
    # 집합 S = num[1:] 
    num = list(map(int, input().split()))

    k = num[0]
    s = num[1:]
    if k==0:
        break
    # del s[0]

    for case in list(combinations(s, 6)):
        print(*case)

    dfs(0, 0)
    print()
