import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# 엑셀 파일 경로 설정
file_path = "C:/CookAnalysis/Excel/singer_youtube.xlsx"

# 엑셀 파일 읽기
df = pd.read_excel(file_path)

# 유튜브 조회수가 높은 순으로 정렬
sorted_df = df.sort_values(by='유튜브 조회수', ascending=False)

# 파이썬 산점도 그래프 그리기
plt.figure(figsize=(10, 6))

# 원의 크기 설정을 위해 조회수 제곱근 계산
sizes = np.sqrt(sorted_df['유튜브 조회수'])

# 다양한 색상 사용을 위해 컬러맵 지정
colors = np.random.rand(len(sorted_df))

plt.scatter(sorted_df['아이디'], sorted_df['유튜브 조회수'], s=sizes, c=colors, alpha=0.5)

plt.title('유튜브 조회수에 따른 가수 산점도 그래프')
plt.xlabel('아이디')
plt.ylabel('유튜브 조회수')
plt.xticks(rotation=45)

# 가로 세로 선 제거
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

plt.grid(True)

plt.show()
