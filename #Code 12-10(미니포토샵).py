def func_rotate(times) :
    global window, canvas, paper, filename, inImage, outImage, inW, inH, outW, outH
    outW = inW
    outH = inH
    outImage = np.rot90(inImage, k=times, axes=(1,2))
    for i in range(times) :
        outW, outH = outH, outW
    display()