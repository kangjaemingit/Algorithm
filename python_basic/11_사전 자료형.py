data = dict()
data['사과'] = 'apple'
data['바나나'] = 'banana'
data['코코넛'] = 'Coconut'

print(data)

if '사과' in data:
    print("사과를 키로 가지는 데이터 존재")

key_list = data.keys()
value_list = data.values()
print(key_list)
print(value_list)

for key in key_list:
    print(data[key])
