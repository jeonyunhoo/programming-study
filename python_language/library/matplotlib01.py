# matplotlib_ex.py
# Matplotlib(맷플롯립)란?
# 몇 줄의 코드로 차트, 그래프, 파이 차트, 산점도, 히스토그램, 오류 차트 등을 그릴 수 있다.
# 다양한 데이터를 많은 방법으로 도식화 할 수 있도록 하는 파이썬 라이브러리  
# matplotlib을 이용하면  numpy나 pandas에서 사용되는 자료구조를 쉽게 시각화 할 수 있다

# 터미널에서 설치 : pip install matplotlib
import matplotlib.pyplot as plt  # matplotlib 라이브러리의 pyplot 모듈을 plt라는 이름으로 import

# 한글 깨짐 방지
plt.rcParams['font.family'] = "Malgun Gothic"  # 맑은 고딕 글꼴 설정
plt.rcParams['axes.unicode_minus'] = False   # 축에 있는 마이너스 기호가 깨지는 것을 방지

# 데이터 설정 및 그래프 그리기
x_values = [1, 2, 3, 4]  # x 값
y_values = [3, 6, 10, 12]  # y 값

plt.plot(x_values, y_values, "o--")  # 스타일 : 'o--' (동그라미 마커 + 점선)
plt.title("기본 선 그래프")           # 그래프 제목
plt.xlabel("x 축")                   # X축 라벨
plt.ylabel("y 축")                   # Y축 라벨


plt.savefig("my_graph.png", dpi=300, bbox_inches='tight')
# - "my_graph.png" : 저장할 파일 이름 및 확장자 (.png, .jpg, .pdf 가능)
# - dpi=300        : 해상도 설정 (300 이상이면 선명한 고화질)
# - bbox_inches='tight' : 축 라벨이나 제목 등 여백이 잘리지 않도록 자동 정돈

# 화면에 그래프 표시
plt.show()