a,b,c,d = map(int, input().split())

if a >= c and a <= d:
    print("Yes")
    exit()
if a <= c and b >= d:
    print("Yes")
    exit()
if b >= c and b <= d:
    print("Yes")
    exit()
if c <= a  and b <= d:
    print("Yes")
    exit()
else:
    print("No")
