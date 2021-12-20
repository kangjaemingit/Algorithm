#while
i = 1
result = 0

while i<= 9:
    result += i
    i += 1

print(result)

#for
result = 0

for i in range(1, 10):
    result += i

print(result)

scores = [90, 80, 77, 65, 97]

for i in range(5):
    if scores[i] >= 80:
        print(i + 1, "합격")

#continue
black_list = {2, 4}

for i in range(5):
    if i + 1 in black_list:
        continue
    if scores[i] >= 80:
        print(i + 1, "합격")

#중첩
for i in range(2, 10):
    for j in range(1, 10):
        print(i, "x", j, "=", i*j)
