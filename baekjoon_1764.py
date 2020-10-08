import sys

N, M = map(int, input().split())

A = set()
B = set()

for i in range(N):
  A.add(input())
for i in range(M):
  B.add(input())

result = sorted(list(A & B))

print(len(result))

for e in result:
  print(e)

