print("*args로 여러개의 값을 받기")

class Calc:
    def add(self, *nums):
        tot = 0
        for i in nums:
            # 튜플에서 속성을 하나씩 꺼내 끝까지 반복
            tot += i
        return tot
    
c = Calc()
print(c.add(10,20))
print(c.add(10,20,30))
print(c.add(10,20,30,40,50))

# ================================
#isinstance(값, 자료형)
# 값이 해당 자료형인지 확인
#결과가 True/False

class Type_class:
    def t_data(self, data):
        if isinstance(data, int):
            print(f"정수: {data}")
        elif isinstance(data, str):
            print(f"문자열: {data}")
        elif isinstance(data, list):
            print(f"리스트: {data}")
        else:
            print("존재하지 않는 자료형입니다.")

t = Type_class()
t.t_data(100)
t.t_data("홍길동")
t.t_data([10,20,30,40])
t.t_data(102.5)