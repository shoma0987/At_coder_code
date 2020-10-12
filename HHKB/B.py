h,w = map(int, input().split())

count = 0
total_pack = []
for i in range(h):
    s =input()
    t = []
    total_pack.append(s)
    for j in range(len(s)-1):
        if s[j] == s[j+1]: count+=1

print(total_pack)
# for k in range(w):
#     for l in range(w-1):
#         if total_pack[l][l] == total_pack[l+1][l]:


