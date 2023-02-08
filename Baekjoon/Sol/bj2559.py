# 투 투포인터 알고리즘 문제
# 백준 2559 문제
# 연속된 며칠 동안의 온도 합 최대값 찾기

import sys
input = sys.stdin.readline

result =[]

n, k = map(int,input().split())
a = list(map(int, input().split()))

for i in range(n - k + 1):
    result.append(sum(a[i:i+k]))
        
print(max(result))