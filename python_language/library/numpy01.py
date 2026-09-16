# Numpy(Numerical Python,넘파이) 란? 
# 파이썬 라이브러리로써, 고성능의 수치계산을 위해 제작,  벡터 및 행렬 연산에 있어서 매우 편리한 기능을 제공함

# 터미널에서 설치: pip install numpy

import numpy as np #numpy 라이브러리를 불러와서 np라는 명칭을 부여함

# numpy 배열 선언
arr= np.array([2,1,5,3,7,4,6,8]) #외장함수
print(arr)

# numpy정렬
arr= np.sort(arr)   # [1 2 3 4 5 6 7 8]
print(arr)

arr1=np.array([1,2,3,4])
arr2=np.array([5,6,7,8])
# 2개의 배열을 합침
arr3=np.concatenate((arr1,arr2)) # [1 2 3 4 5 6 7 8]
print(arr3)

# 배열 연산 (각요소마다 각각 더해짐)
arr11 = arr1+10
print("arr11",arr11)  # arr11 [11 12 13 14]

# 배열의 같은위치끼리 계산
arr12=arr1-arr2
print("arr12",arr12)  # arr12 [-4 -4 -4 -4]

#배열 슬라이싱(특정 인덱스 범위 접근하기)
arr4=np.array([10,20,30,40,50,60,70,80,90,100])
print(arr4[:2])  # 0~1번 인덱스->10,20
print(arr4[1:2]) # 1~1번 인덱스->20
print(arr4[3:8]) # 3~7번 인덱스->40,50,60,70,80
print(arr4[6:])  # 6번인텍스 부터 마지막->70,80,90,100