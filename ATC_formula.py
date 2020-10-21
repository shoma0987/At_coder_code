
#1: 縦にint型 or str型で複数inputをしたい時
N = int(input())
l = []
for i in range(N):
    i = input()
    l.append(i)

#2: 横にint型 or str型で複数inputをしたい時(2パターン)
H, W, K = map(int, input().split()) #数字の場合
H, W, K = input().split()　#文字の場合

A = [int(x) for x in input().split()]
A = list(map(int, input().split()))

H, W = map(int, input().split())
mass = [input() for _ in range(H)] # ex: mass = ["shoma","yusuke"]
# mass[1][1] = "u"  / mass[0][4] = "a"

#連続したintを1文字づつlistに格納する方法(strに変形して打ち込む)
A = 2244858
B = list(str(A))

#3: ある選択肢(リスト)からK個をランダムに選ぶ時(import random)
import random
A = [] #listの中に複数の選択肢が入っている
for i in range(K):
    i = random.choice(A)

#4: listの中の要素の個数を数えたい時、もしくは特定の文字の数を数えたい時(Len関数 or count を使う)
A = [1,2,1,2,2,4,3,2,]
b = len(A)
c = A.count()

#5: append/pop/sort/reverse メソッド
items = [2,3,1,4,5]

items.append(4) #listの最後に指定した文字を追加する
items.pop() #listの中の指定した要素を削除、（）ならば最後の要素を削除する
items.sort() #listを順番に並び替える
items.reverse() #listの要素をひっくり返す
items.clear() #listの全要素削除
items.insert(3, 5) #index[3]に5を追加

print(items)

#6: rangeで繰り返した物をlistに治める方法(いろいろなパターンがある)
my_array1 = [i for i in range(15)]
my_array2 = [[i] for i in range(15)]
my_array3 = [random.randint(1,100) for i in range(15)]
my_array4 = list((x,y) for x in range(1,5) for y in range(5,10) if x !=y)
print(my_array1)

#7: 横一列に文字を出力する方法
a = int(input())
b = int(input()) % 3
c = "{}\t{}".format(a,b)
print(c)

#8: Listの中にある要素のindexを抽出(スタート０)
list = [1,5,7,9]
print(list.index(9))
# printすると"3"を返す

#9: C XYX Triplets問題

n = int(input())
ans = [0 for _ in range(10050)]
# 以上で作れるのは[0,0,0,0,0,,,,,,,]のlist。これcountとして利用
# 範囲を決めて全探索を実施
for i in range(1,105):
    for j in range(1,105):
        for k in range(1,105):
            v = i*i+j*j+k*k+i*j+j*k+k*i;
            if v<10050:
                ans[v]+=1
            #全探索の結果、Nの範囲以下(今回は10050)となったvがあれば、indexを用いてlistのcountを追加

for i in range(n):
    print(ans[i+1]) #ans[0]は使用しないため、[1]から出力

#10 enumarete型(indexを左に表示してループ)
# iがインデックスでjがlistの要素、i+1とすることでindex1から表示できる
l = ["s","K","R"]
for i, j in enumerate(l):
    print(i+1, j)

#11 アルファベットを列挙する方法(a~zとA~Z)
print([chr(ord('a') + i) for i in range(26)])
print([chr(ord('A') + i) for i in range(26)])

#12 ABC171(QuestionC) ある数をNを入力したときに、アルファベットを返せ(ex3:c、27:aa)
N = int(input())
ans = ''
while N > 0:
    ans += chr(ord('a') + N % 26-1)
    # 26で割れば余りは0~26の範囲になるので、それをトリガーに格桁のアルファベットが決まっていく。
    # -1で引いているのは"a"からスタートしているため
    N //= 26 #　N=0になるまで26で割り続ける
print(ans[::-1]) # ループによって蓄積したansのアルファベットを逆から出力

#13 数字列のlistおいて、どの数字がいくつかを集計するCoutner
from collections import Counter
A = [1,1,2,2,3,4,5]
b = Counter(A)
print(b) # ({1: 2, 2: 2, 3: 1, 4: 1, 5: 1})
print(b[2]) #2
print(b.keys()) #左側を全て取り出す
print(b.values()) #右側を全て取り出す

#14 横一列に結果を出力する時
a = [1,2,3,4]
for i in a:
    print(i,end= " ") # 1 2 3 4

#15 好きな10進数をN進数に変えて文字列出力
def card_conv(x,r):
    d = ""
    dchar = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    while x > 0:
        d += dchar[x % r]
        x //= r
    return d[::-1]

#16 条件満たし次第強制プログラムを強制終了させたいとき
(計算量を大幅に減らすことができる)
import sys
a = [0,1,2]
if o in a:
    print("finish")
    sys.exit()

#17 Queueをlistに適用
from collections import deque

a = deque(["s","h","o"])
a.append("m")
a.append("a")
a.popleft()
a.popleft()
print(a)

#18 a^k を m　で割った答え(繰り返し２乗法)

pow(a,k,m)
#以下一応証明:
"""""
def a_k_mod_m(a,k,m):
    b = 1
    for i in reversed(bin(k)[2:]):
        if i == "1": # i ="0"ならスキップ
            b = a * b % m
            l.append(b)
        a = a**2 % m
    return b
"""

#19 入力文字に対応した番号をlistに格納する。
s,t = input().split()
char = "abcdefghijklmnopqrstuvwxyz"
A = list(s)+list(t)
A = list((char.index(i)+1) for i in A)

#20　重複なしの全列挙 (5つの数から重複なしで数字を3つ取り出すときに合計が９になるのは何通りか)
N = 5
count = 0
for i in range(1, N+1):
    for j in range(i+1,N+1):
        for k in range(j+1,N+1):
            if i + j + K == 9:
                count +=0
print(count)

#21 find関数について(該当がない場合-1、第二引数)
S = "1241359"
print(S.find("8")) # -1　
print(S.find("1",3)) #4 (第二引数でindex[3]から探索を始める)

#22 素数抽出法(計算量を考慮すると10000くらいまでが限界)
prime = []
for i in range(2,10000):
    count = 0
    for j in range(2,i+1):
        if i % j == 0:
            count += 1
    if count == 1:
        prime.append(i)

print(prime)
print(len(prime))

#23 10 * 10の行列を作る
matrix = [[0] * n for i in range(n)]

#23 複数の集合を作り、さらにそのうち連結成分が最大の集合の個数を抽出する(BFSの一種)
from networkx import *

G = Graph()
G.add_edges_from([(3,4)]) #3-4を生成
G.add_edges_from([(3,5)]) #3-4-5を生成(5を追加しただけ)
G.add_edges_from([(1,2)]) #1-2を生成
print(len(max(connected_components(G), key=len)))
# 1-2 or 3-4-5の連結成分の大きい方、3-4-5の個数"３"を答えに出す

#24 非常に最速で約数を全て列挙できる関数
def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    divisors.sort()
    return divisors

# 25  listの中にあってif文該当があるやつ全てのindexを列記する
b = [2,3,45,3,5,3,2,45,3,2]
r = [k for k, x in enumerate(b) if x == max(b)]
print(r) # [2,7]

# 26  アルファベットが与えられて、数字に変化させる
alpha_num = lambda c: ord(c) - ord('a') + 1
alpha_num("c") # 3

# 27 Listの中にある、欲しい値のindexを入手する
c = [2,4,2,1,54,5,3]
cc = c.index(54) #4

