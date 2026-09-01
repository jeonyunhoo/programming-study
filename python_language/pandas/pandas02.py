import pandas as pd

# 시리즈(1차원) 선언

# 성적 다루는 간단한 예제

num = [1,2,3,4,5]
score_java = pd.Series([98,76,60,85,80], index = num)
score_python = pd.Series([88,92,100,55,70], index = num)

print(score_java)
print(score_python)

totoal = score_python + score_java
print(f"덧셈 결과는: {totoal}")

print("index 기준 내림차순 정렬")
print(totoal.sort_index(ascending=False))
print("# 값 기준 오른쪽 정렬")
print(totoal.sort_values(ascending=True))
print("# 값 기준 내림차순 정렬")
print(totoal.sort_values(ascending=False))