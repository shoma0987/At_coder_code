import numpy as np
from collections import Counter

n, w, m = map(int, input().split())
matrix = np.zeros((n,w))
row_count = []
col_count = []

for i in range(m):
    h1,w1 = map(int, input().split())
    h1,w1 = h1-1, w1-1
    matrix[h1, w1] = 1
    row_count.append(h1)
    col_count.append(w1)

max_count = 0
row_v2 = Counter(row_count)
col_v2 = Counter(col_count)
row_v3 = row_v2.most_common()[0][0]
col_v3 = col_v2.most_common()[0][0]

row = matrix[row_v3]
col = matrix[:, col_v3]
count1 = np.count_nonzero(row == 1)
count2 = np.count_nonzero(col == 1)

count3 = count1 + count2
# if matrix[row_v3][col_v3] == 1: count3 -=1

print(max_count)
# max_count = 0
# for j in range(n):
#     for k in range(w):
#         row = matrix[j]
#         count1 = np.count_nonzero(row == 1)
#         col = matrix[:,k]
#         count2 = np.count_nonzero(col == 1)
#
#         count3 = count1 + count2
#         if matrix[j][k] == 1: count3 -=1
#         if count3 > max_count:
#             max_count = count3
#










