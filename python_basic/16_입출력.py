# 입력 기본
n = int(input())

data = list(map(int, input().split()))

data.sort(reverse = True)
print(data)

# n, m, k를 공백으로 구분하여 입력
n, m, k = map(int, input().split())

print(n, m, k)

# sys라이브러리
import sys

data = sys.stdin.readline().rstrip()
print(data)

# 출력 +
answer = 7
print("문자열" + str(answer) + "입니다.")

# 출력 ,
print("문자열", str(answer), "입니다.")

# f-string
print(f"문자열 {answer}입니다.")
