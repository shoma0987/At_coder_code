N, X, T = map(int, input().split())
count = 0

while N >= 0:
    if N >= X:
        N = N - X
        count += T
    else:
        N -= N
        count += T
        if N==0:
            break

print(count)