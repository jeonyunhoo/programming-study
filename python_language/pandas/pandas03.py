import pandas as pd
# 2차원 구조(DataFrame)

score = pd.DataFrame(
    [
    [100, 30, 40, 55, 77], # java
    [25, 67, 90, 43, 52], # python
    [100, 100, 98, 78, 89], # c
    ],
    index=["java", "python", "c"]
)

print(score)
print("\n")

num = [1,2,3,4,5]
score2 = pd.DataFrame(
    {
    "이름": ["홍길동", "박봉춘", "김현식", "윤주", "윤진석"],
    "java": [100, 30, 40, 55, 77],
    "python": [25, 67, 90, 43, 52],
    "c": [100, 100, 98, 78, 89]
    },
    index=num
)
print(score2.head(2))
print(score2.tail(2))

print("index 기준 내림차순 정렬")
print(score2.sort_index(ascending=False))
print(score2.sort_values(by="이름", ascending=True))

score3 = score2.sort_values(by="java", ascending=False)
print(score3)

score3.to_csv("./score.csv", encoding="utf-8-sig")
