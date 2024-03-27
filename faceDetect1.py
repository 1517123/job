from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials
import requests
from PIL import Image, ImageDraw
from io import BytesIO

KEY = '你的face服務金鑰'  #face服務金鑰
ENDPOINT = '你的face服務端點'  #face服務端點

face_client = FaceClient(ENDPOINT, CognitiveServicesCredentials(KEY))  #建立客戶端
face_image = 'https://i.imgur.com/G4cZrJ0.jpg'  #圖片網址
detected_faces = face_client.face.detect_with_url(url=face_image)  #偵測人臉
#print(detected_faces)  #列印人臉物件串列
#print(str(detected_faces[0]))  #列印第1個人臉物件
#print(str(detected_faces[0].face_rectangle))  #列印第1個人臉矩形資訊
if not detected_faces:
    print('未偵測到人臉！')
else:
    #下載圖片檔案
    response = requests.get(face_image)
    img = Image.open(BytesIO(response.content))
    draw = ImageDraw.Draw(img)  #繪製原始圖形
    #繪製人臉矩形
    for face in detected_faces:
        rect = face.face_rectangle
        left = rect.left
        top = rect.top
        right = left + rect.width
        bottom = top + rect.height
        draw.rectangle(((left, top), (right, bottom)), outline='red')
    img.show()  #顯示圖片

