# 测试使用图像处理库 Pillow

# 测试缩放图像
import random

from PIL import Image, ImageFilter, ImageFont, ImageDraw

# 打开图片
im = Image.open('/Users/will/Downloads/a.png')
# 获取图片的尺寸
w, h = im.size
print(w, h)
# 将宽高缩放到50%
im.thumbnail((w // 2, h // 2))
print('Resize image to: %sx%s' % (w // 2, h // 2))
# 加入模糊效果
im2 = im.filter(ImageFilter.BLUR)
im2.save('/Users/will/Downloads/b.png')


# 随机生成验证码

# 随机字母
def randomChr():
    return chr(random.randint(65, 90))


# 颜色随机
def randomColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))


# 随机颜色2:
def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))


img_width = 60 * 4
img_height = 60
image = Image.new('RGB', (img_width, img_height), (255, 255, 255))
# 创建字体对象
font = ImageFont.truetype('Arial.ttf', 36)
# 创建Draw对象
draw = ImageDraw.Draw(image)
# 填充每一个像素
for i in range(img_width):
    for y in range(img_height):
        draw.point((i, y), fill=randomColor())

for t in range(4):
    draw.text((60 * t + 10, 10), randomChr(), font=font, fill=rndColor2())

img = image.filter(ImageFilter.BLUR)
image.save('/Users/will/Downloads/c.png')


