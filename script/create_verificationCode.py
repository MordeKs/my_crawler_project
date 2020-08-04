# -*- encoding: utf-8 -*-
"""
@File    : create_verificationCode.py
@Time    : 2020/8/4 11:28
@Author  : Morde
@Software: PyCharm
@Description: 生成验证码
"""
import random
from PIL import Image, ImageDraw, ImageFont, ImageFilter


def rnd_char():
    # return chr(random.randint(97,122))
    return str(random.randint(0,9))


def rnd_color():
    return (random.randint(64,255),random.randint(64,255),random.randint(64,255))


def rnd_color2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))


def _draw():
    width = 60*4
    height = 60
    image = Image.new('RGB',(width,height))

    font = ImageFont.truetype(r'C:\Windows\Fonts\Segoe Script\segoescb.ttf',36)

    draw = ImageDraw.Draw(image)

    for x in range(width):
        for y in range(height):
            draw.point((x,y),fill=rnd_color())

    for t in range(4):
        draw.text((60*t+10,10),rnd_char(),font=font,fill=rnd_color2())

    image = image.filter(ImageFilter.BLUR) # 模糊
    # image.show()
    image.save('../imgs/code2.jpg','jpeg')


if __name__ == '__main__':
    _draw()