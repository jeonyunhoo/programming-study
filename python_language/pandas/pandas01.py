# 판다스 라이브러리
import pandas as pd # pd라고 명명

# 시리즈(1차원) 선언
series1 = pd.Series([2,4,6,8,10]) # 인덱스는 0~
print(series1)

# index를 지정할 수 있다.
series2 = pd.Series([2,4,6,8,10], index = [1,2,3,4,5])
print(series2)

# range로 index 지정
series3 = pd.Series([2,4,6,8,10], index = range(1,6)) # index는 1~5
print(series3)

# 데이터, index를ㄹ 따로 선언 후 활용
data_value = [1, 34, 35, 6, 345]
index_value = [10, 11, 12, 13, 14]
series5 = pd.Series(data_value, index_value)
print(series5)