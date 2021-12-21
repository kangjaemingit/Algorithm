data = ['A','B','C']

# permutations (r개의 데이터를 뽑아 일렬로 나열하는 모든 경우 계산(순서고려))
from itertools import permutations

result = list(permutations(data, 3))
print(result)

# combinations (r개의 데이터를 뽑아 순서를 고려하지 않고 나열하는 모든 경우 계산)
from itertools import combinations

result = list(combinations(data,2))
print(result)

# product (permutations와 같지만 원소 중복 가능)
from itertools import product

result = list(product(data, repeat=2))
print(result)

# combinations_with_replacement(r개의 데이터를 뽑아 순서를 고려하지 않고 나열(원소 중복))
from itertools import combinations_with_replacement

result = list(combinations_with_replacement(data, 2))
print(result)
