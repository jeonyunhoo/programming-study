# 컴프리헨션
# 반복문과 조건문이 한 줄로
# 간단하게 작성하여 리스트나 딕셔너리, 세트를 만드는 방법
#일반 반복문
numbers = [] # 빈 리스트
for i in range(1, 6): # 1~5 반복
    numbers.append(i)
print(numbers)
# 2) 리스트 컴프리헨션
numbers = [i for i in range(1, 6)]
print(numbers)

# 2. 계산하여 리스트에 저장
# 1) 일반 반복문
mul = []
for i in range(1, 6):
    mul.append(i*i)
print(mul)
# 2) 리스트 컴프리헨션
mul = [i*i for i in range(1, 6)]
print(mul)

# 3. 조건이 있는 리스트 컴프리헨션
# 기본 형식
# [표현식 for 변수 in 반복할_데이터 if 조건식]
# 1) 일반
even_num = []
for i in range(1, 11):
    if i % 2 == 0 :
        even_num.append(i)
print(even_num)
# 2) 리스트 컴프리헨션
even_num = [i for i in range(1,11) if i % 2 == 0]
print(even_num)

# 4. 문자열 컴프리헨션
# 1) 리스트 컴프리헨션
names = ["Marcin", "Tim henson", "Ichika Nito"]
lengths = [len(a) for a in names]
print(lengths)
# 2) 일반 문장
lengths2 = []
for a in names:
    lengths2.append(len(a))
print(lengths2)

# 길이가 5개 이상인 단어만 저장, 리스트 컴피리헨션
words = ["apple", "banana", "kiwi", "pear"]
result = [a for a in words if len(a) >= 5]
word_count = len(result)
print(result)
print(word_count)
# 개수 출력 할 수 있도록 추가

# if와 else가 모두 있는 리스트 컴프리헨션
# 기본 형식
# [참일_때_값 if 조건식 else 거짓일_때_값 for 변수 in 반복할_데이터]

res = ["짝수" if i % 2 == 0 else "홀수" for i in range(1, 11)]
print(res)

# 딕셔너리 컴프리헨션
# 딕셔너리 컴프리헨션

# 딕셔너리는 키: 값의 형태로 저장합니다.

# 기본 형식
# {키: 값 for 변수 in 반복할_데이터}

squars = {i:i*i for i in range(1,6)}
print(squars)

# 조건이 있는 딕셔너리 컴프리헨션
# 점수가 80 이상인 학생만 저장
scores = {

    "김철수": 85,
    "이영희": 70,
    "홍길동": 90
}

pass_s = {i:j for j,i in scores.items()}
print(pass_s)

# 테스트
# 1~10 숫자의 3배(*3)로 리스트를 만드시오
mul_num = [i*3 for i in range(1, 11)]
print(mul_num)

even_num = [i for i in range(1,21) if i % 3 == 0]
print(even_num)

res_num = [i if i % 3 == 0 else 0 for i in range(1,21)]
print(res_num)

# 딕셔너리에서 나이가 30이상 회원만 새로운 딕셔너리에 저장
memb = {

    "김철수": 35,
    "이영희": 20,
    "홍길동": 48
}

a = {i:j for i,j in memb.items() if j >= 30}
print(a)