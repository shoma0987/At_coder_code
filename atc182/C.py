
N = input()

x = []
for i in range(0,len(N)):
  x.append(int(N[i]))

k = 1
if sum(x)%3 == 0:
  print(0)
  exit()

else:
  while k < len(N):
    for j in range(0,len(N)-k+1):

      if (sum(x)-sum(x[j:j+k])) % 3 == 0:
        print(k)
        exit()
    k += 1

print(-1)