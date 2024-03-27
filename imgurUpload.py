import json 
import requests 
from base64 import b64encode 

headers = {"Authorization": "Client-ID 你的Client ID"}  #imgur的ClientID
app_token = '你的App Token'  #imgur的app token

url = "https://api.imgur.com/3/upload.json" 
#上傳圖片
try:
    response = requests.post(
        url, 
        headers = headers, 
        data = { 
         'key': app_token, 
         'image': b64encode(open('media/bear1.jpg', 'rb').read()), 
         'type': 'base64', 
         'name': 'bear1.jpg', 
         'title': 'ehappy_bear1' 
        } 
    ) 
    data = json.loads(response.text)['data']
    #print(data])  #顯示回傳值
    print(data['link'])  #圖片網址
except:
    print('上傳圖片失敗！')


