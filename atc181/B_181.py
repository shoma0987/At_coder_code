n = int(input())
count = 0
for i in range(n):
    a,b= map(int,input().split())
    if (b-a+1) % 2 != 0:
        count += (a+b)/2 * (b-a+1)
    else:
        count += (a+b) * (b-a+1)/2
print(int(count))