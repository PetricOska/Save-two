def func_zoomin() :
    global window, canvas, paper, filename, inImage, outImage, inW, inH, outW, outH
    scale = askinteger("확대", "배율-->", minvalue=-2, maxvalue=8)
    outW = inW * scale
    outH = inH * scale
    outImage = np.empty((3,outH, outW), dtype=np.uint8)
    for rgb in range(3) :
        for i in range(outH) :
            for k in range(outW) :
                outImage[rgb][i][k] = inImage[rgb][int(i/scale)][int(k/scale)]
    display()

def func_zoomout() :
    global window, canvas, paper, filename, inImage, outImage, inW, inH, outW, outH
    scale = askinteger("축소", "배율-->", minvalue=-2, maxvalue=8)
    outW = int(inW / scale)
    outH = int(inH / scale)
    outImage = np.empty((3, outH, outW), dtype=np.uint8)
    for rgb in range(3):
        for i in range(outH):
            for k in range(outW):
                outImage[rgb][i][k] = inImage[rgb][int(i * scale)][int(k * scale)]
    display()