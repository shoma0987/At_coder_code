# 仮コード

from collections import Counter

n = input()
if len(n) <= 2:
    # n = "5" or n = "23"とかなら以下処理
    if int(n) % 8 == 0 or int(n[::-1]) % 8 == 0:
        print("Yes")
    else:
        print("No")
    exit()

#nをそのまま数え上げる
cnt = Counter(n) #Counter({'1': 1, '2': 1, '3': 1, '4': 1, '5': 1, '6': 1, '7': 1, '8': 1})

# if not とは
# if notとは if notは条件式の結果が真であれば偽、偽の場合は真を返す演算子です。
# そのため、通常のif文の条件式と異なり、条件が成立しない場合にif文の処理を
# 実施したい場合や条件が成立しなかった値を取得したい場合に使用します

for i in range(104, 1000, 8): #104-112-120-128-132,,,,と進めていって、cntの組み合わせでその数字が作れれば終了
    if not Counter(str(i)) - cnt:
        print("Yes")
        exit()

print("No")