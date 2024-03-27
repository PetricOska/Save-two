from tkinter import *
from PIL import Image, ImageTk

window = Tk()

# PIL로 이미지를 열고 Tkinter에서 사용할 수 있는 형식으로 변환
image = Image.open("C:/Users/hihi1/Pictures/photo/no.jpg")
photo = ImageTk.PhotoImage(image)

label1 = Label(window, image=photo)
label1.pack()

window.mainloop()
# jpg를 사용 했을 때와 gif를 사용 했을 때와 코드가 다릅니다. 유이 하시길...