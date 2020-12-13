import math
import statistics

n = int(input())
a = list(map(int, input().split()))
lists = []

def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    divisors.sort()
    return divisors

for i in range(n):
    lists += make_divisors(a[i])

while True:
    if 1 in lists:
        lists.remove(1)
    else: break

mode = statistics.mode(lists)
print(mode)


