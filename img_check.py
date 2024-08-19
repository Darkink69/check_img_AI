import requests
import json
from fake_useragent import UserAgent
import random
import time
import os
from gradio_client import Client
import useNudeNet
import useBase64
import useCoco
from PIL import Image, ImageDraw, ImageFilter, ImageFont


folder = 'images'
font_size = 15


def draw_result_on_img(img, description):
    im = Image.open(f'{folder}/{img}')
    # print(f"Width: {im.width}")
    # print(f"Height: {im.height}")
    # print(f"Filename: {im.filename}")
    # print(f"Format: {im.format}")
    # print(f"Mode: {im.mode}")

    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype("micross.ttf", size=font_size)
    draw.text(
        (10, 10),
        description,
        font=font,
        fill=('#ffffff')
    )
    for count, value in enumerate(result):
        color = ['#FFCC00', '#F7931E', '#ED5BED', '#48CCC6', '#29ABE2', '#E4B9F9', '#FC5454', '#80CCFF', '#FFCC00']
        box = result[count]['box']
        draw.rectangle((box[0], box[1], box[0] + box[2], box[1] + box[3]), outline=(color[count]), width=2)
        draw.text(
            (box[0], box[1] - 20),
            f"{result[count]['class']} - {round(result[count]['score'], 2) * 100}%",
            font=font,
            fill=(color[count])
        )

    im.save(f"result/{img}")


files = os.listdir(folder)
print(f"Files {len(files)} in folder {folder}")

for img in files:
    description = useCoco.get_coco_response(f'{folder}/{img}')
    print(description)

    try:
        result = useNudeNet.get_nude_net(f'{folder}/{img}')
    except BaseException:
        result = []
    print(result)

    try:
        draw_result_on_img(img, description)
    except BaseException:
        print(f'Failed to open file {img}')

    print('--------------------------------------')



# for j in result:
#     if j['class'] in all_labels and j['score'] > .2:
#         print(j)
        # print(result)








# all_labels = [
#     "FEMALE_GENITALIA_COVERED",
#     "FACE_FEMALE",
#     "BUTTOCKS_EXPOSED",
#     "FEMALE_BREAST_EXPOSED",
#     "FEMALE_GENITALIA_EXPOSED",
#     "MALE_BREAST_EXPOSED",
#     "ANUS_EXPOSED",
#     "FEET_EXPOSED",
#     "BELLY_COVERED",
#     "FEET_COVERED",
#     "ARMPITS_COVERED",
#     "ARMPITS_EXPOSED",
#     "FACE_MALE",
#     "BELLY_EXPOSED",
#     "MALE_GENITALIA_EXPOSED",
#     "ANUS_COVERED",
#     "FEMALE_BREAST_COVERED",
#     "BUTTOCKS_COVERED",
# ]

# analysis_labels = [
#     "FEMALE_GENITALIA_COVERED",
#     "FACE_FEMALE",
#     "BUTTOCKS_EXPOSED",
#     "FEMALE_BREAST_EXPOSED",
#     "FEMALE_GENITALIA_EXPOSED",
#     "MALE_BREAST_EXPOSED",
#     "ANUS_EXPOSED",
#     "FEET_EXPOSED",
#     "BELLY_COVERED",
#     "FEET_COVERED",
#     "ARMPITS_COVERED",
#     "ARMPITS_EXPOSED",
#     "FACE_MALE",
#     "BELLY_EXPOSED",
#     "MALE_GENITALIA_EXPOSED",
#     "ANUS_COVERED",
#     "FEMALE_BREAST_COVERED",
#     "BUTTOCKS_COVERED",
# ]
#
# nsfw_labels = [
#     "BUTTOCKS_EXPOSED",
#     "FEMALE_BREAST_EXPOSED",
#     "FEMALE_GENITALIA_EXPOSED",
#     "ANUS_EXPOSED",
#     "FEET_EXPOSED",
#     "BELLY_EXPOSED",
#     "MALE_GENITALIA_EXPOSED",
# ]

bad_words = ['a', 'the', 'of', 'and', 'from', 'to', 'that', 'with', 'is', 'by', 'in', 'on', '.', '?', ',', '!',
                 'are', 'at', 'it', 'front', '[', ']', '(', ')', '-', 'an', 'for', 'into', 'am', '', '"', '`', "'",
                 "'s", 'there', 'has', 'who', 'his', 'I']

nsfw_words = ['bikinisuit', 'bikini', 'bikinis', 'panties', 'pantiesis', 'bra', 'bodysuit', 'underwear', 'stripped',
              'undressed', 'unclothed', 'naked', 'nude', 'bare', 'stark-naked', 'disrobed', 'unclad', 'undraped',
                  'unsheathed', 'breasts', 'breast', 'breasty', 'topless', 'boobs', 'nipples', 'nipple', 'butt', 'ass',
                  'sex', 'sexual', 'sexy', 'uncensored', 'lingerie', 'lingersuit', 'nightgown', 'sauna']



# print('Создаем новый каталог')
# path = os.getcwd()
# f = open("img_catalog.txt", "w")
# for root, dirs, files in os.walk(path):
#     for file in files:
#         img_path = f'{root}/{file}\n'
#         f.write(img_path)
#         print(img_path)
# f.close()

# img = Image.open("C://Users/varkatov\Downloads/trash//nu.png")
