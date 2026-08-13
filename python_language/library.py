import math
import random

num = 25

print(f"제곱근: {math.sqrt(num)}")
print(f"2의 3제곱: {math.pow(2,3)}")
print(f"원주율: {math.pi}")

student = ["홍길동", "권율", "유관순", "세종"]

# random.choice: 리스트 내부에서 무작위 추출
sel = random.choice(student)
# random.randint: 지정된 값 사이에서 무작위 정수 추출
dice = random.randint(1,6)

print(f"발표할 학생: {sel}")
print(f"주사위 숫자: {dice}")