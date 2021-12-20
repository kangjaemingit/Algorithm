score = 85

#pass
if score >= 80:
    pass
else:
    print('성적이 80점 미만입니다.')

print('프로그램을 종료합니다.')


#한줄 소스
if score >= 80: result = "Success"
else: result = "fail"
print(result)

#조건부 표현식
result = "Success" if score >= 80 else "Fail"
print(result)

#조건부 표현식x
a = [1, 2, 3, 4, 5, 5, 5]
remove_set = {3, 5}

result = []
for i in a:
    if i not in remove_set:
        result.append(i)

print(result)

#조건부 표현식o
result = [i for i in a if i not in remove_set]

print(result)
