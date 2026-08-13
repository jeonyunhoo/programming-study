# raise: 오류를 일부러 발생
# throw: 오류를 일부러 발생
# throws: 호출한 곳으로 오류 처리하도록 던짐

age = 5
if age <= 0:
    raise ValueError("나이가 0보다 작거나 같을 수 없습니다.")
print(f"나이는 {age}")

try:
    age = int(input("나이를 입력해주세요: "))
    if age <= 0:
        raise ValueError("나이가 0보다 작거나 같을 수 없습니다.")
    
except ValueError as e:
    print(f"오류: {e}")

else:
    print(f"나이: {age}")

finally:
    print("프로그램을 종료합니다.")