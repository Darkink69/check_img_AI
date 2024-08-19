import requests
from gradio_client import Client
import useBase64


def get_coco_response(img):
    print('Waiting blip-2 API...')
    try:
        client = Client("http://127.0.0.1:7860/")
        result = client.predict(img, api_name="/predict")
        # print(result)
        return result
    except BaseException:
        print('No local server. Waiting Huggingface...')
        base64_string = useBase64.convert_to_base64(img)
        url = 'https://2chch-git-large-coco.hf.space/run/predict'
        # url = 'https://freddyaboulton-git-large-coco.hf.space/run/predict'
        try:
            response = requests.post(url, json={
              "data": [f"data:image/png;base64,{base64_string}"]}).json()
            # print("!!!!!", response["data"][0])
            return response["data"][0]
        except BaseException:
            return ""
