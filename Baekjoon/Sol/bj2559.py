'''
구간합 구하기
슬라이싱 [i:i+k] 와 같이 구하면 슬라이싱에 해당하는 원소들을 복사하여 새로운 객체를 생성하기에 원소수에 비례하는 시간이 걸린다.

tip.
1. 가장 처음의 구간합을 구한다.
2. 첫번째 원소는 빼고 다음 원소는 더하는 식으로 구간합을 이어가면서 최대값 찾는다.
'''
import sys

input = sys.stdin.readline

# n: 온도 측정 전체 날짜 (2이상) N개의 온도라고 이해
# k: 연속적인 날짜의 수 (1과 N)
n, k = map(int, input().split())

day = list(map(int, input().split()))


cur = sum(day[:k])
ans = cur

# k부터 n까지 (2부터 10까지)
for i in range(k, n):
    #void.append(sum(day[i:i+k])) #  슬라이싱은 복사때문에 원소가 많을수록 오래걸린다.
    #     #max_temp = max(max_temp, sum(day[i:i+k]))
    
    # 첫원소 빼고 마지막원소 더하기
    #cur = cur + 
    #print(i, i-k)
    cur = cur - day[i-k] + day[i]
    ans = max(cur, ans)

print(ans)
#print(max(void))