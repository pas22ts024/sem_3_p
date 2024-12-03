from PIL import Image
image = Image.open("img1.bmp")
pixels = list(image.getdata())
for i in range(len(pixels)):
    new_rgb = list(pixels[i])
    for j in range(3):
        tec = bin(new_rgb[j])[2:]
        inverse = ''
        for k in tec:
            if k == '0':
                inverse += '1'
            else:
                inverse += '0'
        inverse = int(inverse, 2)
        new_rgb[j] = inverse
    pixels[i] = tuple(new_rgb)
new_image = Image.new(image.mode, image.size)
new_image.putdata(pixels)
new_image.save("inverse.bmp")
