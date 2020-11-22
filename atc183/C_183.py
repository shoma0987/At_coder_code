from itertools import permutations
#自力で完成セールスマン問題

n,k1 = map(int, input().split())

pp = [x for x in range(2, n+1)]
# 全てのコストが入っている。
lists = [list(map(int, input().split())) for i in range(n)]

# print(lists)

perm = permutations(pp)
perm1 = []
for k in list(perm):
    perm1.append(list(k))
# print(perm1)

perm2 = []
for i in range(len(perm1)):
    perm2.append(list("1"))
    for j in range(len(pp)):
        perm2[i].append((perm1[i][j]))
    perm2[i].append(1)


for l in range(len(perm2)):
    perm2[l][0] = 1

# print(perm2) #これで全道順のルート完成
# print(len(perm2))


ans = 0
for m in range(len(perm2)):
    total_cost = 0
    for n in range(len(perm2[0])-1): #lists = 0~3
        total_cost += lists[perm2[m][n]-1][perm2[m][n+1]-1]
    if total_cost == k1:
        ans += 1

print(ans)


