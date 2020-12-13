
# r1=a, c1=b, r2=c, c2=d
r1,c1 = map(int, input().split())
r2,c2 = map(int, input().split())
# a+b = c+d
# a-b = c-d
# |a-c| = |b-d| <= 3
count = 0
e = r2 - c2
