result = []

N = int(input())
K = int(input())

data = list()
for i in range(N):
  data.append(i+1)

flag = K - 1

while True:
  result.append(data.pop(flag))  
  if not data:
    break
  flag = (flag + K - 1) % len(data)

print(result)
