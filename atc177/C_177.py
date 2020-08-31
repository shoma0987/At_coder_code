n = int(input())
nums = list(map(int ,input().split()))
total = 0

for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        k = (nums[i] * nums[j])
        total += k
print(total % (10**9+7))

