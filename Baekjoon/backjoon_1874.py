n = int(input())
arr = list()
stack = list()
answer = list()

for i in range(n):
    t = int(input())
    arr.append(t)

arrnum = 0
stacknum = 2
stack.append(1)
print("+")

while len(answer) < n:
    if arr[arrnum] == stack[-1]:
        answer.append(stack.pop())
        print("-")
        arrnum += 1
    else:
        stack.append(stacknum)
        print("+")
        stacknum += 1
    #print(answer)