import csv  # CSV 파일을 다루기 위한 모듈을 임포트합니다.
import time  # 시간과 관련된 기능을 사용하기 위한 모듈을 임포트합니다.
import datetime  # 날짜와 시간을 다루기 위한 모듈을 임포트합니다.

csvName = 'C:/CookAnalysis/CSV/daterime.csv'  # CSV 파일의 경로를 변수에 저장합니다.
with open(csvName, 'w', newline='') as csvFp:  # CSV 파일을 쓰기 모드로 엽니다.
    csvWriter = csv.writer(csvFp)  # CSV 파일에 데이터를 쓰기 위한 writer 객체를 생성합니다.
    csvWriter.writerow(['연월일', '시분초'])  # CSV 파일의 첫 번째 줄에 열 제목을 씁니다.

count = 10  # 반복 횟수를 지정합니다.
while count > 0:  # count가 0보다 큰 동안 반복합니다.
    count -= 1  # 반복 횟수를 감소시킵니다.

    now = datetime.datetime.now()  # 현재 시간을 가져와서 now 변수에 저장합니다.
    yymmdd = now.strftime('%Y-%m-%d')  # 현재 날짜를 '연-월-일' 형식으로 변환합니다.
    hhmmss = now.strftime('%H:%M:%S')  # 현재 시간을 '시:분:초' 형식으로 변환합니다.
    time_list = [yymmdd, hhmmss]  # 날짜와 시간을 리스트에 저장합니다.
    print(time_list)  # 날짜와 시간을 출력합니다.

    with open(csvName, 'a', newline='') as csvFp:  # CSV 파일을 추가 모드로 엽니다.
        csvWriter = csv.writer(csvFp)  # CSV 파일에 데이터를 쓰기 위한 writer 객체를 생성합니다.
        csvWriter.writerow(time_list)  # CSV 파일에 날짜와 시간을 씁니다.

    time.sleep(3)  # 3초간 대기합니다.
