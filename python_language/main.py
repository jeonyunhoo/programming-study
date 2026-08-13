# 1) import calculator #.py는 쓰지 않는다
# 2) import calculator as cal
# 3) from calculator import * # *: 모든 함수
from calculator import add, sub
num1 = 100
num2 = 6

# 1) print(f"더하기: {calculator.add(num1, num2)}")
# 1)print(f"빼기: {calculator.sub(num1, num2)}")
# 2) print(f"곱하기: {cal.mul(num1, num2)}")
# 3) print(f"나누기: {divi(num1, num2)}")
print(f"더하기: {add(num1, num2)}")
print(f"빼기: {sub(num1, num2)}")