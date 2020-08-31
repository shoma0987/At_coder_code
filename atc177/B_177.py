# 他人のコードにて勉強
S = input()
T = input()

ans = len(T)

for i in range(len(S) - len(T) + 1):
    tmp = len(T)
    for j in range(len(T)):
        if T[j] == S[i + j]:
            tmp -= 1
            ans = min(ans, tmp)
print(ans)
