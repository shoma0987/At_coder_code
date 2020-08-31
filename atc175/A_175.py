S = input()
s = list(S)
 
count = 0
max_count = 0
 
for i in s:
    if i == "R":
        count += 1
    else: 
        if max_count <= count:
            max_count = max(max_count,count) 
        count =0
if max_count <= count:
    max_count = count
print(max_count)
