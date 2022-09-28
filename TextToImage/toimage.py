import os
from PIL import Image, ImageDraw, ImageFont
FOLDER_PATH = os.path.abspath(os.path.dirname(__file__))


def __text_to_img(text: str, image_wight: int = 512) -> Image:
    font_path = os.path.abspath(os.path.join(FOLDER_PATH, 'STHUPO.TTF'))
    if not os.path.exists(font_path):
        raise ValueError('Font not found')

    # 处理文字层 主体部分
    font_main_size = image_wight // 25
    font_main = ImageFont.truetype(font_path, font_main_size)
    # 按长度切分文本
    spl_num = 0
    spl_list = []
    for num in range(len(text)):
        text_w = font_main.getsize_multiline(text[spl_num:num])[0]
        if text_w >= image_wight * 0.78:
            spl_list.append(text[spl_num:num])
            spl_num = num
    else:
        spl_list.append(text[spl_num:])
    test_main_fin = ''
    for item in spl_list:
        test_main_fin += item + '\n'

    text_w, text_h = font_main.getsize_multiline(test_main_fin)

    image_height = text_h + 100

    text_main_img = Image.new(mode="RGBA", size=(
        image_wight, text_h), color=(0, 0, 0, 0))

    ImageDraw.Draw(text_main_img).multiline_text(
        xy=(0, 0), text=test_main_fin, font=font_main, fill=(0, 0, 0))

    # 初始化背景图层
    background = Image.new(mode="RGB", size=(
        image_wight, image_height), color=(255, 255, 255))

    # 向背景图层中置入文字图层
    background.paste(im=text_main_img, box=(
        image_wight // 10, 50), mask=text_main_img)

    return background


def text_to_img(text: str, image_wight: int = 512):
    image = __text_to_img(text, image_wight)
    image.save("C:/jihuang/Jiqiren/go-cqhttp/data/images/new_car.jpg")
