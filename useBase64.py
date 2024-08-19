import base64


def convert_to_base64(img):
    with open(img, 'rb') as image_file:
        base64_bytes = base64.b64encode(image_file.read())
        # print(base64_bytes)

        base64_string = base64_bytes.decode()
        # print(base64_string)

    return base64_string
