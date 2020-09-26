
n,x,m = map(int, input().split())
mod = 0
sqr = x
for i in range(n):
    mod += sqr % m
    sqr = pow(sqr,2)

print(mod)
