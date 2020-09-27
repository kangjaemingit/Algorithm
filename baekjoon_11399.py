
N = int(input())
time = list(map(int, input().split()))

time.sort()
total = 0
temp = 0

for i in range(N):
    temp = temp + time[i]
    total = total + temp

print(total)