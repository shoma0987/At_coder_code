#Lは12以上

stick = 11
L = int(input())-1
L2 = L-11
L3 = min(stick,L2)

ans = 1
for i in range(L3):
    ans *= (L-i)
for j in range(L3):
    ans //= (j+1)

print(int(ans))