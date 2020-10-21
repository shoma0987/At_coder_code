#他人のコード

# x= 強さ、y = 進化のための経験値、a = * a、b = + b
x,y,a,b = map(int,input().split())
ans = 0
for i in range(10**9):

    if x * a < b:
        x *= a
    else:
        # divmod = 引数2つ与えて、商と余を得る関数
        div,mod = divmod((y - x),b)
        ans += div
        if mod == 0:
            ans -= 1
        break

    if x >= y:
        break
    #以下はif文に該当しようがしまいが、毎ターンカウント
    ans += 1
print(ans)