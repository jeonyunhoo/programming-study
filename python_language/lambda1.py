# 1. 람다 함수란?

# 람다 함수는 "이름이 없는 짧은 함수"입니다.
# 일반 함수는 def를 사용하지만,
# 람다 함수는 lambda라는 단어를 사용합니다.
#람다 함수는 짧고 간단한 계산에 적합합니다.

# 일반 함수 형식#
# def 함수이름(매개변수):
#     return 계산식

# 람다 함수 형식#
# lambda 매개변수: 계산식
print("일반 함수와 람다 함수 비교")
print('=' * 60)

def Double(x): # 매개변수
    return x * 2

b = lambda x: x*2

# b = Double(10)
print(Double(10)) # a(인수) 보냄
print(b(10))

print('=' * 60)
print("거듭제곱 람다 함수 비교")
print('=' * 60)
# 5의 제곱 10의 제곱

square = lambda x: x ** 2
print("5의 제곱",square(5))
print("10의 제곱",square(10))

# +, * 람다함수( 인수를 2개 - 매개변수 2개)
print('=' * 60)

add = lambda x,y: x + y
mul= lambda x,y: x * y

print("10 + 20 = ",add(10,20))
print("4 * 5 = ",mul(4,5))

print('=' * 60)
print("조건식이 들어간 람다 함수")
print('=' * 60)

res = lambda x : "짝수" if(x % 2== 0) else "홀수"

print(res(4))
print(res(5))

print("=" * 60)
print("매개변수가 없는 람다 함수")
h = lambda : "안녕하세요"
print(h())

# 10과 60 중에 큰 값을 구하는 람다 함수

res = lambda x, y : f"{x}이 더 큽니다" if(x > y) else f"{y}이 더 큽니다"
print(res(10, 60))

# map()은 리스트의 값을 하나씩 꺼내
# 같은 계산을 반복할 때 사용합니다.
#
# 형식
# map(함수, 리스트)
#
# map()의 결과는 바로 리스트가 아니기 때문에
# list()를 사용하여 리스트로 바꿉니다.

number = [1, 2, 3, 4, 5]

result = list(map(lambda x : x * 2, number))
print(f"원본: {number}")
print(f"결과: {result}")

print("map() 으로 점수를 5점 올리기")
score = [78, 89, 91, 56]

score_res = list(map(lambda x : x + 5, score))
print(f"원본: {score}")
print(f"결과: {score_res}")

# filter()는 조건에 맞는 값만 골라냅니다.
#
# 형식
# filter(조건 함수, 리스트)
#
# 람다 함수의 계산 결과가 True이면 남기고,
# False이면 제외합니다.

num = [10, 33, 45, 26, 40, 88]

res = list(filter(lambda x : x % 3 == 0, num))
# 람다 함수 매개변수 x가 리스트에서 한 개씩 가져오는데
# 람다 함수 내 표현식(3의 배수)이 맞는다면 결과에 포함
# 람다 함수 내 표현식(3의 배수)이 옳지 않다면 포함하지 않음
# 결과를 list에 반영(변경)
print(res)

# filter()이용하여 합격점수 구하기(70점 이상)
jumsu = [45, 60, 90, 77, 55]
res = list(filter(lambda x : x >= 70, jumsu))
print(res)