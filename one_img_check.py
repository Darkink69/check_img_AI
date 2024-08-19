from gradio_client import Client
import useNudeNet
import useBase64
import useCoco
from PIL import Image, ImageDraw, ImageFilter, ImageFont


folder = 'images'


bad_words = ['a', 'the', 'of', 'and', 'from', 'to', 'that', 'this', 'with', 'is', 'by', 'in', 'on', '.', '?', ',', '!', ':', 'are', 'at', 'it', 'front', '[', ']', '(', ')', '-', '|', 'an', 'for', 'into', 'am', '', '"', '`', "'", "'s", 'there', 'has', 'who', 'his', 'I', 'i', '#', 'so', 'unused0', '&', 'this', "]'s", '],', '##0']

nsfw_labels = [
    "BUTTOCKS_EXPOSED",
    "FEMALE_BREAST_EXPOSED",
    "FEMALE_GENITALIA_EXPOSED",
    "ANUS_EXPOSED",
    "FEET_EXPOSED",
    "BELLY_EXPOSED",
    "MALE_GENITALIA_EXPOSED",
]

nsfw_words = ['bikinisuit', 'bikini', 'bikinis', 'panties', 'pantiesis', 'bra', 'bodysuit', 'underwear', 'stripped',
              'undressed', 'unclothed', 'naked', 'nude', 'bare', 'stark-naked', 'disrobed', 'unclad', 'undraped',
              'unsheathed', 'breasts', 'breast', 'breasty', 'topless', 'boobs', 'nipples', 'nipple', 'butt', 'ass',
              'sex', 'sexual', 'sexy', 'uncensored', 'lingerie', 'lingersuit', 'nightgown', 'sauna', 'sunbathing',
              'sunbath']

def get_description(img):
    nsfw = False
    description = useCoco.get_coco_response(f'{folder}/{img}')
    desc = description.split(' ')
    tags = []
    for i in desc:
        if i not in bad_words:
            tags.append(i.rstrip("."))
        if i in nsfw_words:
            nsfw = True
            print('nsfw contain in DESCRIPTION!')
    print(description)
    print(tags)


    try:
        nude_net = useNudeNet.get_nude_net(f'{folder}/{img}')
        for item in nude_net:
            if item['class'] in nsfw_labels:
                nsfw = True
                print('nsfw contain in NUDE_NET!')
                print(item)
    except BaseException:
        nude_net = []

    print(nude_net)

    return description, tags, nude_net, nsfw



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








