from tkinter import*
from tkinter import messagebox

## 함수 선언 부분 ##
def myFunc() :
    if chk.get() == 0 :
        messagebox.showinfo("","체크버튼이 꺼졌어요.")
    else :
        messagebox.showinfo("","체크버튼이 커졌어요.")

## 메인 코드 부분 ##
window = Tk()

chk = IntVar()
cb1 = Checkbutton(window, text = "클릭하세요", variable = chk, command = myFunc)

cb1.pack()

window.mainloop()
