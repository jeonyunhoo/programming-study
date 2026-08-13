class SimpleBook:
    def __init__(self, title, price):
        self.title = title
        self.price = price

    def __str__(self):
        return f"도서명: {self.title}, 가격: {self.price}"

s = SimpleBook("Python 기초", 20000)
print(s)
# s라는 객체를 출력하로 하면 자동으로 __str__ 함수를 호출함
# __str__() 함수: 원하는 포맷으로 출력을 원할 때 사용
# __str__() 함수: 문자열로 return 함