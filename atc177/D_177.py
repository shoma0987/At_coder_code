from networkx import *
n,m = map(int, input().split())
if m == 0: print(1);exit()
G = Graph()
for i in range(m):
    a,b = map(int, input().split())
    G.add_edges_from([(a,b)])

print(len(max(connected_components(G), key=len)))
# key=lenは長さを比較してくれる

#以下他人のコード
# from networkx import *
# N, M = map(int, input().split())
# if M == 0:
#     print(1)
#     exit()
# else:
#     A = [list(map(int, input().split())) for m in range(M)]
#     G = Graph()
#     G.add_edges_from(A)
#     print(len(max(connected_components(G), key=len)))