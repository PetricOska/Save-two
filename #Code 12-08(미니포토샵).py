def func_gray() : 
    global window, canvas, paper, filename, inImage, outImage, inH, inW, outH, outW
    ## 중요! 출력 영상 크기 결정 ##
    outH = inH
    outW = inW
    inImage = inImage.astype(np.int16)
    grayImage = (inImage[0] + inImage[1] + inImage[2]) / 3    # 2차원 배열
    grayImage = np.concatenate((grayImage, grayImage, grayImage))
    outImage = np.reshape(grayImage, (3,outH, outW))
    outImage = outImage.astype(np.uint8)
    inImage = inImage.astype(np.uint8)
    display()

def func_bw1(): 
    global window, canvas, paper, filename, inImage, outImage, inW, inH, outW, outH
    outW = inW
    outH = inH

    inImage = inImage.astype(np.int16)
    grayImage = (inImage[0] + inImage[1] + inImage[2]) / 3 # 2차원 배열
    grayImage = np.concatenate((grayImage, grayImage, grayImage))
    outImage = np.reshape(grayImage, (3, outH, outW))
    outImage = np.where(outImage < 128, 0, 255)
    outImage = outImage.astype(np.uint8)
    inImage = inImage.astype(np.uint8)
    display()

def func_bw2() : 
    global window, canvas, paper, filename, inImage, outImage, inW, inH, outW, outH
    outW = inW
    outH = inH
    inImage = inImage.astype(np.int16)
    grayImage = (inImage[0] + inImage[1] + inImage[2]) / 3 # 2차원 배열
    grayImage = np.concatenate((grayImage, grayImage, grayImage))
    outImage = np.reshape(grayImage, (3, outH, outW))
    value = np.mean(outImage)
    outImage = np.where(outImage < value, 0, 255)
    outImage = outImage.astype(np.uint8)
    inImage = inImage.astype(np.uint8)
    display() 