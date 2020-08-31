N = int(input())
n = str(N)
list = [i for i in n]
plus = 0

for j in list:
    plus += int(j)

if plus % 9 == 0:
    print("Yes")
else:
    print("No")
