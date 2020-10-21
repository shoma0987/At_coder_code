# 問題文
# 頂点にラベルが付き辺にはラベルが付いていないN頂点M辺の単純とも連結とも限らないグラフであって、
# 以下の条件を満たすものの個数を 10^9+7で割ったあまりを求めてください。
# ・自己ループを持たない
# ・すべての頂点の次数が2以下である
# ・各連結成分のサイズを並べたとき、その最大値がちょうどLである

# 入力　N(ノード数:識別できる) M(辺の数) L(連結最大の数)
from scipy.special import comb
# a = comb(n, r)
import math
from itertools import combinations

n,m,l = map(int, input().split())
all_node = []
for i in range(1,n+1):
    all_node.append(i)

com = comb(len(all_node),l)

per = math.factorial(l) // 2

mod = 10^9 + 7
fa1 = com/mod
fa2 = per/mod

print(fa1 * fa2 * mod)

