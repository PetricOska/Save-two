def func_bright() :
    global window, canvas, paper, filename, inImage, outImage, inH, inW, outH, outW
    outH = inH
    outW = inW
    value = askinteger("밝게", "값-->", minvalue=-1, maxvalue=255)
    inImage = inImage.astype(np.int16)
    outImage = inImage + value
    outImage = np.where(outImage > 255, 255, outImage)
    outImage = outImage.astype(np.uint8)
    inImage = inImage.astype(np.uint8)
    display()

    def func_dark() :
        global window, canvas, paper, filename, inImage, outImage, inH, inW, outH, outW
        outH = inH
        outW = inW
        value = askinteger("어둡게", "값-->", minvalue=-1, maxvalue=255)
        inImage = inImage.astype(np.int16)
        outImage = inImage - value
        outImage = np.where(outImage < 0, 0, outImage)
        outImage = outImage.astype(np.uint8)
        inImage = inImage.astype(np.uint8)
        display()