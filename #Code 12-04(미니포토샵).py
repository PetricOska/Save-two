def display() : 
    global window, canvas, paper, filename, inImage, outImage, inW, inH, outW, outH

    if canvas != None:
        canvas.destroy()

    window.geometry(str(outW) + 'x' + str(outH))
    canvas = Canvas(window, width=outW, height=outH)
    paper = PhotoImage(width=outW, height=outH)
    canvas.create_image((outW / 2, outH / 2), image=paper, state='normal')

    rgbString = ""
    for i in range(0, outH):
        tmpString = ""
        for k in range(0, outW):
            dataR = outImage[0][i][k]
            dataG = outImage[1][i][k]
            dataB = outImage[2][i][k]
            tmpString += "#%02x%02x%02x " % (dataR, dataG, dataB) # x 뒤에 한 칸 공백
        rgbString += "{" + tmpString + "} "                       # } 뒤에 한 칸 공백
    paper.put(rgbString)
    canvas.pack()

def func_open() : 
    global window, canvas, paper, filename, inImage, outImage, inW, inH, outW, outH
    filename = askopenfilename(parent=window, filetypes=(("Color 파일", \
                               "*.jpg;*.png;*.bmp;*.tif;"), ("모든파일", "*.*")))

    photo = Image.open(filename)  # PIL 객체
    inW = photo.width
    inH = photo.height
    inImage = np.empty((3, inH, inW), dtype=np.uint8)

    photoRGB = photo.convert('RGB’)
    for i in range(inH):
        for k in range(inW):
            r, g, b = photoRGB.getpixel((k, i))
            inImage[0][i][k] = r
            inImage[1][i][k] = g
            inImage[2][i][k] = b

    outW = inW
    outH = inH
    outImage = inImage.copy()
    display()