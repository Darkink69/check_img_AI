import json
import requests
import one_img_check
import datetime as dt
import os
import uni_telegram_bot


# os.system('app.py')
site = 'jazzradio'
chat_id = "813012401"
json_files = os.listdir(f'json/{site}')
print(f"{len(json_files)} json-files in folder {site}")


def time_now():
    return dt.datetime.now().strftime("%H:%M:%S")


for json_file in json_files:
    print(f'Start {json_file}')
    data = json.load(open(f"json/{site}/{json_file}", "r", encoding='utf-8'))
    print(len(data))
    msg = f'Start {json_file} - {len(data)}'
    # uni_telegram_bot.send_message(chat_id, msg)

    for index, i in enumerate(data):
        if "description_cover" not in i:
            try:
                url = f'http:{i["art_url"]}'
                print(url)
                response = requests.get(url)
                img = f'{i["art_url"][-37:]}.jpg'
                # print(img)
                with open(f'images/{img}', 'wb') as file:
                    file.write(response.content)
            except BaseException:
                print('No url')

            description, tags, nude_net, nsfw = one_img_check.get_description(img)

            if nsfw:
                uni_telegram_bot.send_photo_file(chat_id, f'images/{img}')
                msg = f'{i["track"]} - {index}/{len(data)}\n {json_file}\n {nude_net}'
                uni_telegram_bot.send_message(chat_id, msg)

            try:
                del i["network_id"]
                del i["display_artist"]
                del i["display_title"]
                del i["duration"]
                del i["started"]
                del i["type"]
                del i["images"]
                i["description_cover"] = description
                i["description_tags"] = tags
                i["nude_net"] = nude_net
                i["nsfw"] = nsfw
            except BaseException:
                print('Error', i)

            with open(f"json/{site}/{json_file}", "w", encoding='utf-8') as file:
                json.dump(data, file, indent=2, ensure_ascii=False)

        print(time_now(), '----------------------------------------', index, '/', len(data))


# print(data)





