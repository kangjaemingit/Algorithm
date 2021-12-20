n = int(input())
answer = 0

arr = list()

while(True):
  arr.append(n%3)

  if n//3 == 0:
    break
  
  n = n//3

for i in range(len(arr)):
  answer += arr.pop() * (3**i)

print(answer)

