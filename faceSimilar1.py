from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials
import requests
from PIL import Image, ImageDraw
from io import BytesIO

KEY = '你的face服務金鑰'  #face服務金鑰
ENDPOINT = '你的face服務端點'  #face服務端點

face_client = FaceClient(ENDPOINT, CognitiveServicesCredentials(KEY))  #建立客戶端
#取得單一人臉
single_face_image = 'https://i.imgur.com/y8tXb5t.jpg'
detected_faces = face_client.face.detect_with_url(url=single_face_image)
if not detected_faces:
    print('單一人臉圖片未偵測到人臉！')
else:
    single_face_id = detected_faces[0].face_id
    #取得多個人臉
    multi_face_image = "https://i.imgur.com/G4cZrJ0.jpg"  #多個人臉含相同人臉
    #multi_face_image = "https://i.imgur.com/jFjfgHn.jpg"  #多個人臉不含相同人臉
    #multi_face_image = "https://i.imgur.com/bfhb0ML.jpg"  #相同單一人臉
    detected_faces2 = face_client.face.detect_with_url(url=multi_face_image)
    if not detected_faces2:
        print('多個人臉圖片未偵測到人臉！')
    else:
        #取得多張人臉的ID
        multi_face_ids = []
        for face in detected_faces2:
            multi_face_ids.append(face.face_id)
        similar_faces = face_client.face.find_similar(face_id=single_face_id, face_ids=multi_face_ids) #尋找類似臉部
        #print(similar_faces)  #列印類似人臉物件串列
        #print(str(similar_faces[0]))  #列印類似人臉物件內容
        if len(similar_faces) == 0:
            print('未偵測到類似人臉！')
        else:
            print("找到類似人臉！")

            #下載圖片檔案
            response = requests.get(multi_face_image)
            img = Image.open(BytesIO(response.content))
            draw = ImageDraw.Draw(img)
            for face in similar_faces:
                #取得類似人臉
                for x in detected_faces2:
                    if x.face_id == face.face_id:
                        face_info = x
                #畫出矩形
                left = face_info.face_rectangle.left
                top = face_info.face_rectangle.top
                right = left + face_info.face_rectangle.width
                bottom = top + face_info.face_rectangle.height
                draw.rectangle(((left, top), (right, bottom)), outline='red')
            img.show()

