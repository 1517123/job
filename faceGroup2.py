from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials

KEY = '3d05dfce570142fa90adbe2fe3dcd31f'  #face服務金鑰
ENDPOINT = 'https://asfasfa.cognitiveservices.azure.com/'  #face服務端點

face_client = FaceClient(ENDPOINT, CognitiveServicesCredentials(KEY))  #建立客戶端
PERSON_GROUP_ID = 'ehappygroup'  #人員群組名稱

#由檔案讀入人員名稱與ID字典
f = open('ehappy.txt', 'r')
persondict = eval(f.read())
f.close()

face_ids = []  #要測試的人臉串列
#取得人臉
test_face_image = 'https://i.imgur.com/Njs2iFy.jpg'  #含bear圖片
#test_face_image = 'https://i.imgur.com/osa4VAo.jpg'  #不含人員圖片
#test_face_image = 'https://i.imgur.com/3Q2ykft.jpg'  #含jeng,david圖片
detected_faces = face_client.face.detect_with_url(url=test_face_image)
for face in detected_faces:
    face_ids.append(face.face_id)
#識別人臉是否在人員群組中
identify_face = face_client.face.identify(face_ids, PERSON_GROUP_ID) 
#print(identify_face)
#print(identify_face[0].candidates[0].person_id)

personNum = 0  #存人員總數
for i, person in enumerate(identify_face):
    if len(person.candidates) != 0:  #包含人員
        list1 = list(persondict.keys())  #將字典key轉為串列
        n = list(persondict.values()).index(person.candidates[0].person_id)  #由人員ID取得串列索引
        print('圖片人臉包含 {}'.format(list1[n]))
        personNum += 1
if personNum == 0:
    print('沒有人員群組中的人員！')


