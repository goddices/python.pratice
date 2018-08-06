from PIL import Image
# im = Image.new('RGB', (100, 100), 0xFFFFFF)
# for i in range(100):
#     im.putpixel((i,i),0x123123)
# im.show()


img2 = Image.new('RGB', (5, 5), 0xFFFFFF)
# pxdat = [(1, 1, 0xDDDDDD), (2, 2, 0xDDDDDD), (3, 3, 0xDDDDDD),
#          (4, 4, 0xDDDDDD), (0, 0, 0xDDDDDD)]
# for i in range(5):
#     img2.putpixel((i, i), 0x0000FF)
# b = img2.tobytes()

img2.putdata([(0xFF,0x0,0xFF),(0xFF,0x0,0xFF),(0xFF,0x0,0xFF),(0xFF,0x0,0xFF),(0xFF,0x0,0xFF)])
img2.show()
print('aaa')
