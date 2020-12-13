import copy

n,m,t = map(int, input().split())
A = [list(map(int, input().split())) for i in range(m)]

n2 = copy.deepcopy(n)
current = 0

while True:
    for i in range(m):
        if n - (A[i][0]-current) > 0:
            n -=  (A[i][0]-current)
            current = A[i][1]
        else:
            print("No")
            exit()
        if n2 != n:
            if  n +(current-A[i][0]) >n2:
                n = n2
            else:
                n +=(current-A[i][0])

    if n > (t - current):
        print("Yes")
        exit()
    else:
        print("No")
        exit()

