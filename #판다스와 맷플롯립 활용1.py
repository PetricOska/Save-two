import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# 입력 파일 경로와 출력 파일 경로 정의
inFilename = 'C:/CookAnalysis/Excel/singer.xlsx'
outFilename = 'C:/CookAnalysis/Excel/singer_over6.xlsx'

# 엑셀 파일에서 'senior'와 'junior' 시트 읽어오기
df_senior = pd.read_excel(inFilename, 'senior', index_col=None)
df_junior = pd.read_excel(inFilename, 'junior', index_col=None)

# 'senior'와 'junior' 데이터프레임 합치기
df_singer = pd.concat([df_senior, df_junior])

# 인원이 6명 이상인 가수들의 데이터프레임 추출
df_singer_over6 = df_singer[df_singer['인원'] >= 6]
df_singer_over6 = df_singer_over6.sort_values(by=['인원'], axis=0, ascending=False)
df_singer_over6 = df_singer_over6.loc[:, ['아이디', '이름', '인원', '유튜브 조회수']]

# 막대 그래프를 그리기 위한 데이터 준비
x_data = df_singer_over6['아이디']
y_data = df_singer_over6['인원']
colorAry = [np.random.choice(['red', 'green', 'blue', 'brown', 'gold', 'lime', \
                              'aqua', 'magenta', 'purple']) for _ in range(len(x_data))]

# 막대 그래프 그리기
plt.bar(x_data, y_data, color=colorAry)
plt.show()

# 출력 파일로 데이터프레임 저장
writer = pd.ExcelWriter(outFilename)
df_singer_over6.to_excel(writer, sheet_name='singer', index=False)
writer.save()

print('Save. OK~')