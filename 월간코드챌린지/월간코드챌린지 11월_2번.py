s = "110010101001"
answer = [0,0]
temp = []
count_change = 1
count_one = s.count('1')
count_zero = s.count('0')
   
while(count_one > 1):
  
  while(count_one > 0):
    temp.insert(0, count_one % 2)
    count_one = count_one // 2

  for i in range(len(temp)):
    if temp.pop() == 0:
      count_zero = count_zero + 1
    else:
      count_one = count_one + 1
      
  count_change = count_change + 1
        
answer[0] = count_change
answer[1] = count_zero

print(answer)