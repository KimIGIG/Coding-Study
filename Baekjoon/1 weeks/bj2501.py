N, M = map(int, input().split())

cnt = 0
ans = 0
for i in range(1, N+1):
    if (N % i == 0):
        cnt += 1 
    if cnt == M:
        ans = i 
        break
if ans:
    print(ans)
else:
    print(0)