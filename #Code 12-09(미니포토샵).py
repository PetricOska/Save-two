def func_mirror1() :
    global window, canvas, paper, filename, inImage, outImage, inW, inH, outW, outH
    outW = inW
    outH = inH
    outImage = np.flip(inImage,axis=1)
    display()

def func_mirror2() :
    global window, canvas, paper, filename, inImage, outImage, inW, inH, outW, outH
    outW = inW
    outH = inH
    outImage = np.flip(inImage, axis=2)
    display()