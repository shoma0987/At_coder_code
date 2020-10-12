n = int(input())
p = list(map(int, input().split()))

count = 0
min = 0
for i in range(n):
    if count == 0 and p[i] > 0:
        print(0)
    elif
