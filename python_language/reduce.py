from functools import reduce

print("reduce 함수와 람다 함수")

# reduce()는 앞에서부터 두 값을 계산하고,
# 그 결과를 다음 값과 다시 계산
# lambda a, b: a + b
# 1단계: a=1, b=2  → 1+2 = 3
# 2단계: a=3, b=3  → 3+3 = 6
# 3단계: a=6, b=4  → 6+4 = 10
# 4단계: a=10, b=5 → 10+5 = 15
number = [10,30,50,20,60]

sum = reduce(lambda a,b : a+b, number)
print("결과는: ", sum)