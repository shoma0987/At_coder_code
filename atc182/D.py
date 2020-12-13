# 入力
N = int(input())
A = list(map(int, input().split()))

# 初期化
sum = 0
addmax = 0
now = 0
ans = 0

# for
for i in A:
    sum += i
    if (sum > addmax):
        addmax = sum

    if (now + addmax > ans):
        ans = now + addmax

    now += sum
print(ans)