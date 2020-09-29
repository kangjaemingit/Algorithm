N = int(input())

arr = list()
cnt = 0;
end = 0;

for i in range(N) :
    x, y = map(int, input().split())
    arr.append([x, y])

arr.sort(key = lambda x: (x[1], x[0]))

for j in range(len(arr)):
    if end <= arr[j][0]:
        end = arr[j][1]
        cnt += 1

print(cnt)