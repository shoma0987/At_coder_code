#あとで答え合わせ

n,m = map(int, input().split())
A = list(map(int, input().split()))

if n==1 and m==0:
    print(1)
    exit()
if n==m:
    print(0)
    exit()

Binary = list(0) * n #([0,0,0,0,1,0,0,0,1])
for j in range(len(A)):
    Binary[A[j]-1] = 1

count =
for k in range(len(Binary)):


