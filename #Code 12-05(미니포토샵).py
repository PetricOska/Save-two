def func_save() : 
    global window, canvas, paper, filename, inImage, outImage, inW, inH, outW, outH
    saveFp = asksaveasfile(parent=window, mode='wb', defaultextension='*.jpg', \
                           filetypes=(("JPG 파일", "*.jpg"), ("모든 파일", "*.*")))
    if saveFp == '' or saveFp == None:
        return
    photoRGB = Image.new('RGB', (outW, outH))
    for i in range(outH):
        for k in range(outW):
            r, g, b = outImage[0][i][k], outImage[1][i][k], outImage[2][i][k]
            photoRGB.putpixel( (k,i), (r, g, b, 255))
    photoRGB.save(saveFp.name)