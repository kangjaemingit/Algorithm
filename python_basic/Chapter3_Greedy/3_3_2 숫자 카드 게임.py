n, m = map(int, input().split())

result = 0

for i in range(n):
  data = list(map(int, input().split()))
  value = 10001

  for a in data:
    value = min(value, a)
  
  result = max(result, value)

print(result)