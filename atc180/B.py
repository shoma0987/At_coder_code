import math

n = int(input())
x = list(map(int, input().split()))

#マンハッタン
c1 = 0
c2 = 0
for j in x:
    c1 += abs(j)
    c2 += pow(j,2)

x1 = []
for k in x:
    x1.append(abs(k))

print(c1)
print(math.sqrt(c2))
print(max(x1))