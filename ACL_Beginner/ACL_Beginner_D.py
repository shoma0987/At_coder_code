n,k = map(int, input().split())

list = []
list2 = list
for i in range(n):
    a = int(input())
    list.append(a)
count = 0
for j in range(len(list)-1):
    if abs(list[j] - list[j+1]) <= 3:
        pass
    else: list.pop(max(list2[j] , list2[j+1]))


print(n-count)