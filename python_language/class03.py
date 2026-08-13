print("상속, super, 오버라이딩, 다형성")
# 부모 클래스
class Employ:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def work(self):
        print(f"{self.name}이(가) 일합니다.")
    
    def print_info(self):
        print(f"이름: {self.name}")
        print(f"급여: {self.salary}만 원")

# 자식 클래스
class Developer(Employ):
    def __init__(self, name, salary, language):
        # 부모 생성자 호출
        super().__init__(name, salary)
        # 자식만 있는 변수
        self.language = language
    # 오버라이딩(재정의)
    def work(self):
        print(f"{self.name} 개발자가 {self.language}프로그램을 작성합니다.")

    def print_info(self):
        super().print_info
        print(f"언어: {self.language}")

# 자식 클래스 2
# 선생님, 과목(subject)
class Teacher(Employ):
    def __init__(self, name, salary, subject):
        super().__init__(name,salary)
        self.subject = subject
    
    def work(self):
        print(f"{self.name} 선생님이 {self.subject}과목을 수업하십니다ㅏ.")
    
    def print_info(self):
        super().print_info()
        print(f"과목: {self.subject}")

dev = Developer("홍길동", 450, "Python")
tea= Teacher("김길동", 550, "Math")

print(f"개발자 정보")
dev.print_info()
print(f"\n교사 정보")
tea.print_info()

# ---------------------------------------

print("\n직원들의 업무")
e_list = [
    dev,
    tea
]

for i in e_list:
    i.work()
# 자바의 다형성: 부모 타입의 자식 객체
# 파이썬의 다형성: 객체가 같은 이름의 함수를 가짐
# -> 실행할 때 마다 각가의 서로 다른 객체의 함수가 실행
# 개발자는 개발자의 work()
# 교사는 교사의 work()