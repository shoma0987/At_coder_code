#他人のコードにて学習
s = int(input())
a = list(map(int,input().split()))
mod = 10 ** 9 + 7
ans = 0
sum_a = sum(a) #累積和の考え方を用いる。
#すなわち、今回の問題はあたえられN個全ての整数の組み合わせを作る問題だが、
#通常、組み合わせ総数は(n*(n-1))/2とりO(n^2)の計算量となり間に合わない。
#そこで初めてに全体の和を取ってから、listを前から順に引いていくことで計算量をO(n)まで減らす。

for i in range(s):
    sum_a -= a[i]
    ans += sum_a * a[i]
print(ans%mod)


#以下のマイコードでは、オーバーフローする。
# n = int(input())
# nums = list(map(int ,input().split()))
# total = 0
#
# for i in range(len(nums)):
#     for j in range(i+1,len(nums)):
#         k = (nums[i] * nums[j])
#         total += k
# print(total % (10**9+7))

