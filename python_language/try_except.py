# try:
# 혹시 오류가 있을 지도 모르는 문장 작성
# except:
# 오류가 난다면 오류를 잡음
# else:
# 오류가 발생하지 않을 때 실행
# finally:
# 오류 여부 관계없이 항상 수행

try:
    num = int(input("숫자를 입력하세요: "))
    res=100/num

except ValueError:
    print(f"오류, 숫자를 입력하세요.")
except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
except Exception as e:
    print(f"오류 메시지: {e}")
else:
    print(f"결과는 {res}")
finally:
    print("프로그램 종료")