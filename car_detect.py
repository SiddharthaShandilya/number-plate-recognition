
import cv2, numpy
import matplotlib.pyplot as mpl
model = cv2.CascadeClassifier('haarcascade_russian_plate_number.xml')
cap = cv2.VideoCapture(0)
while True:
    ret,photo = cap.read()
    #if len(photo)==0:
     #   break
    faces = model.detectMultiScale(photo)
    faces = numpy.asarray(faces)
    print(faces.shape)
    #print(photo)
    
    for i in range(faces.shape[0]):
        if len(faces) != 0:
            x1 = faces[i][0]
            y1 = faces[i][1]
            x2 = x1 + faces[i][2]
            y2 = y1 + faces[i][3]
            cropped_pic = cv2.rectangle(photo,(x1,y1),(x2,y2),[0,220,0],5)
        
        
        else:
            cropped_pic = photo
    #face_array = numpy.asarray(faces)
    #cropped_face = detect_face(face_array)
    cv2.imshow('hi',cropped_pic)
    if cv2.waitKey(10)==13:
        break
cv2.destroyAllWindows()
