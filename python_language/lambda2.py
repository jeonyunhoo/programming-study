print("sort()와 람다 함수")
# 리스트와 튜플의 차이점
# 순서 있음: 리스트[], 튜플()
# 순서 없음: 집합{}, => 중복 없음
# 딕셔너리: {} => 키, 값

students = [

    ("홍길동", 60),
    ("권율", 92),
    ("이순신", 88),
    ("유관순", 74)
]

stulist = sorted(students, key=lambda x : x[1])
print(f"오름차순: {stulist}")
for a in stulist: # a에 stulist의 요소를 담는다
    print(a)

stulist = sorted(students, key=lambda x : x[1], reverse=True)
print(f"내림차순: {stulist}")

print("=" *60)

print("딕셔너리 -> 리스트")
stu = [

    {"name": "홍길동", "score": 70},
    {"name": "아이유", "score": 88},
    {"name": "변우석", "score": 95},
    {"name": "유재석", "score": 52}
]

# "name"m "score": 키
# "유재석", 52: 값
# 점수순으로 내림차순
stu_list = sorted(stu, key = lambda x : x["score"], reverse=True)
print("내림차순")
for ss in stu_list:
    print(ss["name"], ss["score"])