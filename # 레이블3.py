from tkinter import *
from PIL import Image, ImageTk

window = Tk()

# jpg 이미지 파일 로드
jpg_image = Image.open("C:/Users/hihi1/Pictures/photo/no5.jpg")
jpg_photo = ImageTk.PhotoImage(jpg_image)

# webp 이미지 파일 로드
webp_image = Image.open("C:/Users/hihi1/Pictures/photo/no6.jpg")
webp_photo = ImageTk.PhotoImage(webp_image)

# 첫 번째 이미지 표시
label1 = Label(window, image=jpg_photo)
label1.pack(side=LEFT)

# 두 번째 이미지 표시
label2 = Label(window, image=webp_photo)
label2.pack(side=LEFT)

window.mainloop()