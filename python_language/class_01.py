# 클래스 변수와 인스턴스 변수
print("클래스 변수와 인스턴스 변수")
# 클래스 변수: (클래스 내부에서)모든 객체가 사용
# 인스턴스 변수: 
class Students:
    s_name = "중앙직업전문학교"

    def __init__(self, name, score): # 자바의 생성자와 유사하다
        self.name = name # 인스턴스 변수
        self.score = score

    def print_info(self):
        print(f"학교: {self.s_name}")
        print(f"이름: {self.name}")
        print(f"점수: {self.score}")

s1 = Students("홍길동", 90) # 객체1 생성
s2 = Students("유관순", 75) # 객체2 생성

s2.score = 99 # 인스턴스 변수의 값을 변경
Students.s_name = "글로벌직업전문학교"

s1.print_info()
s2.print_info()

print(f"학교명: {Students.s_name}")

print("\n" + "="*60)

print("파이썬의 함수 오버로딩")

class Calculator:

    def add(self,a,b):
        return a+b
    
    def add(self,a,b,c=100):
        return a+b+c
    
c1 = Calculator() # 객체 생성
# print(c1.add(10,20,30))
# print(c1.add(100,200))
print(c1.add(10,20, 300))
# 파이썬에서는 같은 이름의 함수를 여러번 작성 하면
# 마지막에 작성한 함수가 앞의 함수를 덮어씀