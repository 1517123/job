from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials
from azure.cognitiveservices.vision.face.models import TrainingStatusType
import time

KEY = '3d05dfce570142fa90adbe2fe3dcd31f'  #face服務金鑰
ENDPOINT = 'https://asfasfa.cognitiveservices.azure.com/'  #face服務端點

face_client = FaceClient(ENDPOINT, CognitiveServicesCredentials(KEY))  #建立客戶端
PERSON_GROUP_ID = 'ehappygroup'  #人員群組名稱
#建立空的人員群組
try:
    face_client.person_group.delete(person_group_id=PERSON_GROUP_ID, name=PERSON_GROUP_ID)
except:
    pass
face_client.person_group.create(person_group_id=PERSON_GROUP_ID, name=PERSON_GROUP_ID)

persondict = {}  #人員名稱與其ID的字典
#建立人員名稱
bear = face_client.person_group_person.create(PERSON_GROUP_ID, "bear")
bear_images = ['https://i.imgur.com/Njs2iFy.jpg', 'https://i.imgur.com/rTT89Zf.jpg']
persondict['bear'] = bear.person_id
david = face_client.person_group_person.create(PERSON_GROUP_ID, "david")
david_images = ['https://i.imgur.com/jFjfgHn.jpg', 'https://i.imgur.com/sTSDxtg.jpg']
persondict['david'] = david.person_id
jeng = face_client.person_group_person.create(PERSON_GROUP_ID, "jeng")
jeng_images = ['https://i.imgur.com/y8tXb5t.jpg', 'https://i.imgur.com/bfhb0ML.jpg']
persondict['jeng'] = jeng.person_id
#將人員名稱字典存入檔案
f = open('ehappy.txt', 'w')
f.write(str(persondict))
f.close()
    
#加入人員圖片
for image in bear_images:
    face_client.person_group_person.add_face_from_url(PERSON_GROUP_ID, bear.person_id, image)
for image in david_images:
    face_client.person_group_person.add_face_from_url(PERSON_GROUP_ID, david.person_id, image)
for image in jeng_images:
    face_client.person_group_person.add_face_from_url(PERSON_GROUP_ID, jeng.person_id, image)

#訓練人員群組
print('開始人員群組訓煉')
face_client.person_group.train(PERSON_GROUP_ID)
while True:
    training_status = face_client.person_group.get_training_status(PERSON_GROUP_ID)
    if (training_status.status is TrainingStatusType.succeeded):
        print('訓練完成！')
        break
    elif (training_status.status is TrainingStatusType.failed):
        print('訓練失敗！')
        break
    time.sleep(5)



