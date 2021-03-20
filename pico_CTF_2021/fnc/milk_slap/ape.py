from PIL import Image

im = Image.open('./concat_v.png')

img_width, img_height = im.size


start = 0
for i in range(0, 66):
    end = start+720
    print((0, start, img_width, end))
    im.crop((0, start, img_width, end)).save(
        './frames/frame{}.png'.format(i), quality=100)
    start += 720
