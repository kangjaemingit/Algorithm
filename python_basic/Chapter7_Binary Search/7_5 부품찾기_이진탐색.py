n = int(input())
nlist = list(map(int, input().split()))
m = int(input())
mlist = list(map(int, input().split()))

def binary_search(array, target, start, end):
  while start <= end:
    mid = (start + end) // 2
    if array[mid] == target:
      return mid
    elif array[mid] > target:
      end = mid - 1
    else:
      start = mid + 1
  
  return None

nlist.sort()

for i in range(m):
  if binary_search(nlist, mlist[i], 0, n -1) == None:
    print("no", end=' ')
  else:
    print("yes", end=' ')
