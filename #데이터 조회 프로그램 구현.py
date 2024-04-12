# sqlite3 모듈 임포트
import sqlite3

# 연결 객체와 커서 객체 초기화
con, cur = None, None

# 데이터를 저장할 변수 초기화
data1, data2, data3, data4 = "", "", "", ""

# 결과 행을 저장할 변수 초기화
row = None

# SQLite 데이터베이스에 연결
con = sqlite3.connect("C:/sqlite/naverDB")

# 커서 객체 생성
cur = con.cursor()

# 사용자 테이블에서 모든 데이터를 선택하는 SQL 쿼리 실행
cur.execute("SELECT * FROM userTable")

# 결과 출력
print("사용자 ID 사용자이름 이메일 출생연도")
print("-------------------------------------")

# 모든 행을 가져와서 출력
while (True) :
    # 결과에서 다음 행을 가져옴
    row = cur.fetchone()
    
    # 더 이상 행이 없으면 반복문 종료
    if row == None :
        break
    
    # 행에서 각 열의 데이터를 변수에 할당
    data1 = row[0]
    data2 = row[1]
    data3 = row[2]
    data4 = row[3]
    
    # 데이터 출력
    print("%5s %15s %20s %d" % (data1, data2, data3, data4))

# 데이터베이스 연결 종료
con.close()
