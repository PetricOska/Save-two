import sqlite3
from tkinter import *
from tkinter import messagebox

# 데이터 입력 함수
def insertData():
    # 데이터베이스 연결 및 커서 생성
    con, cur = None, None
    con = sqlite3.connect("C:/sqlite/naverDB")
    cur = con.cursor()
    
    # 입력한 데이터 가져오기
    data1 = edt1.get()
    data2 = edt2.get()
    data3 = edt3.get()
    data4 = edt4.get()
    
    try:
        # SQL 쿼리 문자열 생성 및 실행
        sql = "INSERT INTO userTable VALUES('{}', '{}', '{}', '{}')".format(data1, data2, data3, data4)
        cur.execute(sql)
        con.commit()  # 데이터베이스에 변경사항 반영
        messagebox.showinfo('성공', '데이터 입력 성공')
    except Exception as e: 
        messagebox.showerror('오류', '데이터 입력 오류가 발생함: ' + str(e))
    
    con.close()  # 데이터베이스 연결 종료

# 데이터 조회 함수
def selectData():
    con = sqlite3.connect("C:/sqlite/naverDB")
    cur = con.cursor()
    cur.execute("SELECT * FROM userTable")
    rows = cur.fetchall()  # 모든 데이터 가져오기

    # 리스트박스 초기화
    listData1.delete(0, END)
    listData2.delete(0, END)
    listData3.delete(0, END)
    listData4.delete(0, END)

    # 컬럼명 추가
    listData1.insert(END, "사용자ID")
    listData2.insert(END, "사용자이름")
    listData3.insert(END, "이메일")
    listData4.insert(END, "출생연도")
    listData1.insert(END, "--------")
    listData2.insert(END, "---------")
    listData3.insert(END, "--------")
    listData4.insert(END, "---------")

    # 데이터 삽입
    for row in rows:
        listData1.insert(END, row[0])
        listData2.insert(END, row[1])
        listData3.insert(END, row[2])
        listData4.insert(END, row[3])
    
    con.close()

# GUI 생성
window = Tk()
window.geometry("600x300")
window.title("GUI 데이터 입력")

# 데이터 입력 프레임 생성
edtFrame = Frame(window)
edtFrame.pack()

# 데이터 조회 프레임 생성
listFrame = Frame(window)
listFrame.pack(side=BOTTOM, fill=BOTH, expand=1)

# 입력 필드 생성
edt1 = Entry(edtFrame, width=10)
edt1.pack(side=LEFT, padx=10, pady=10)
edt2 = Entry(edtFrame, width=10)
edt2.pack(side=LEFT, padx=10, pady=10)
edt3 = Entry(edtFrame, width=10)
edt3.pack(side=LEFT, padx=10, pady=10)
edt4 = Entry(edtFrame, width=10)
edt4.pack(side=LEFT, padx=10, pady=10)

# 입력 버튼 생성
btnInsert = Button(edtFrame, text="입력", command=insertData)
btnInsert.pack(side=LEFT, padx=10, pady=10)

# 조회 버튼 생성
btnSelect = Button(edtFrame, text="조회", command=selectData)
btnSelect.pack(side=LEFT, padx=10, pady=10)

# 리스트박스 생성
listData1 = Listbox(listFrame, bg='yellow')
listData1.pack(side=LEFT, fill=BOTH, expand=1)
listData2 = Listbox(listFrame, bg='yellow')
listData2.pack(side=LEFT, fill=BOTH, expand=1)
listData3 = Listbox(listFrame, bg='yellow')
listData3.pack(side=LEFT, fill=BOTH, expand=1)
listData4 = Listbox(listFrame, bg='yellow')
listData4.pack(side=LEFT, fill=BOTH, expand=1)

window.mainloop()
