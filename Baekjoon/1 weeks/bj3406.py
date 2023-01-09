T = int(input()) # test case

for i in range(T):
    n = int(input())
    n = bin(n)[2:]
    
    for i in range(len(n)):
        if n[-i-1] == '1':
            print(i, end = ' ')