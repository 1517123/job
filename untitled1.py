import numpy as np
import cv2
gc=np.zeros((512,512,3),np.uint8)
gc.fill(200)
cv2.circle(gc,(250,250),100,(0,0,255),5)
cv2.ellipse(gc,(253,300),(40,25),0,0,180,(255,0,0),2)
cv2.ellipse(gc,(253,300),(40,25),0,180,360,(255,0,0),2)
cv2.line(gc,(218,290),(288,290),(255,0,0),2)
cv2.ellipse(gc,(300,220),(30,25),0,180,360,(255,0,0),3)
cv2.ellipse(gc,(210,220),(30,25),0,180,360,(255,0,0),3)
pts=np.array(((253,44),(325,149),(450,152),(390,258),(451,367),(325,369),(252,474),(184,367),(55,367),(117,260),(54,153),(184,147)))
cv2.polylines(gc,[pts],True,(0,255,0),3)
font=cv2.FONT_HERSHEY_SIMPLEX

cv2.putText(gc,'10810529',(50,450),font,3,(0,0,0),2,cv2.LINE_AA)
cv2.imshow('10810529',gc)
cv2.waitKey(0)
cv2.destroyAllWindows()
