n = int(input())
stack = list()

for i in range(n):
    str = input().split()

    if str[0] == 'push':
        stack.append(int(str[1]))

    elif str[0] == 'pop':
        if not stack:
            print('-1')
        else:
            print(stack[-1])
            stack.pop()

    elif str[0] == 'size':
        print(len(stack))

    elif str[0] == 'empty':
        if not stack:
            print('1')
        else:
            print('0')

    elif str[0] == 'top':
        if not stack:
            print(-1)
        else:
            print(stack[-1])