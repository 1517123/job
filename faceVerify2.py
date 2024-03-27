from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials

KEY = '你的face服務金鑰'  #face服務金鑰
ENDPOINT = '你的face服務端點'  #face服務端點

face_client = FaceClient(ENDPOINT, CognitiveServicesCredentials(KEY))  #建立客戶端
face_image1 = 'https://i.imgur.com/y8tXb5t.jpg'
face_image2 = 'https://i.imgur.com/bfhb0ML.jpg'  #相同人
#face_image2 = 'https://i.imgur.com/jFjfgHn.jpg'  #不同人

#取得第一張圖片人臉
detected_faces1 = face_client.face.detect_with_url(face_image1)
image1_id = detected_faces1[0].face_id
#取得第二張圖片人臉
detected_faces2 = face_client.face.detect_with_url(face_image2)
image2_id = detected_faces2[0].face_id

verify_face = face_client.face.verify_face_to_face(image1_id, image2_id)  #人臉比對
#print(verify_face)  #顯示比對結果
if verify_face.is_identical:
    print("兩者為同一人，信心指數：{}".format(verify_face.confidence))
else:
    print("兩者為不同人，信心指數：{}".format(verify_face.confidence))



