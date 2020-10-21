import sys
# xは強さ、yは進化値、aは×、bは+
x,y,a,b = map(int, input().split())
accumilation = 0
x1,x2 = 0,0

while True:

    x1 = (x * a)
    x2 = (x + b)
    x3 = min(x1, x2)

    if x1 > x2:
        x = x2
        if y > x:
            accumilation += 1
            pass
        else:
            print(accumilation)
            sys.exit()

        while True:
            x += x2
            if y > x:
                accumilation += 1
                pass
            else:
                print(accumilation)
                sys.exit()
    x = x3

    if y > x:
        accumilation += 1
        pass
    else: break

print(accumilation)