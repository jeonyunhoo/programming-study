import matplotlib.pyplot as plt  # 시각화 라이브러리인 matplotlib의 pyplot 모듈을 plt라는 별칭으로 불러옴

# 1. 한글 폰트 및 마이너스 기호 깨짐 방지 설정
plt.rcParams['font.family'] = "Malgun Gothic"  # 그래프의 기본 폰트를 Windows용 '맑은 고딕'으로 지정
plt.rcParams['axes.unicode_minus'] = False     # 그래프 축의 마이너스(-) 부호가 깨지는 현상 방지

# 2. 그래프에 사용할 데이터 정의
x = [1, 2, 3, 4, 5]       # X축 공통 데이터 (1부터 5까지)
y1 = [2, 4, 6, 8, 10]     # Y축 첫 번째 데이터 (선형으로 증가)
y2 = [1, 4, 9, 16, 25]    # Y축 두 번째 데이터 (제곱으로 증가)

# 3. 전체 도화지(fig) 및 서브플롯 영역(axes) 생성
# 1행 2열(가로로 2개) 구조로 분할하며, 전체 이미지 크기를 가로 10인치, 세로 4인치로 설정
fig, axes = plt.subplots(1, 2, figsize=(10, 4))

# Axes (개별 그래프): 도화지 안에 들어가는 하나하나의 차트 칸
# 4. 첫 번째 서브플롯(왼쪽 그래프: axes[0]) 작성
axes[0].plot(x, y1, 'r-o', label='선형 증가')  # 'r-o': 빨간색(r), 실선(-), 동그라미 마커(o)로 선 그래프 생성
axes[0].set_title('선형 그래프')             # 왼쪽 그래프의 제목 설정
axes[0].set_xlabel('X 축')                   # 왼쪽 그래프의 X축 라벨 설정
axes[0].set_ylabel('Y 축')                   # 왼쪽 그래프의 Y축 라벨 설정
axes[0].grid(True)                           # 배경에 격자선(그리드) 표시
axes[0].legend()                             # 'label' 속성에 지정한 범례 출력

# 5. 두 번째 서브플롯(오른쪽 그래프: axes[1]) 작성
axes[1].bar(x, y2, color='skyblue', label='제곱 증가')  # 하늘색(skyblue) 막대 그래프 생성
axes[1].set_title('막대 그래프')                       # 오른쪽 그래프의 제목 설정
axes[1].set_xlabel('X 축')                             # 오른쪽 그래프의 X축 라벨 설정
axes[1].set_ylabel('Y 축')                             # 오른쪽 그래프의 Y축 라벨 설정
axes[1].grid(True)                                     # 배경에 격자선(그리드) 표시
axes[1].legend()                                       # 'label' 속성에 지정한 범례 출력

# 6. 레이아웃 정돈 및 화면 출력
plt.tight_layout()  # 서브플롯 간의 간격과 축 라벨 겹침 현상을 자동으로 최적화
plt.show()          # 작성된 완성 그래프를 화면에 표시