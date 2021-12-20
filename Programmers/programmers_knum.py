array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
answer = []

cmdlength = len(commands)

for i in range(cmdlength):
    start = commands[i][0] - 1
    end = commands[i][1]
    temp = []

    for j in range(start, end):
        temp.append(array[j])
    temp.sort()
    answer.append(temp[commands[i][2] - 1])

print(answer)