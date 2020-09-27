K = int(input())
stack = list()
sum = 0

for i in range(K):
  a = int(input())

  if a != 0 :
    stack.append(a)
  elif a == 0 :
    stack.pop()

if not stack :
  print("0")
else :
  for i in range(len(stack)) :
    sum += stack[i]
  print(sum)