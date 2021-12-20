def add (a,b):
    print(a+b)
    return a + b

print(add(3, 7))

# 인수 지정 호출
add(b = 3, a = 1)

# global 키워드
a = 0

def func():
    global a
    a += 1

for i in range(10):
    func()

print(a)

#람다
print((lambda a,b: a + b)(3 ,7))
