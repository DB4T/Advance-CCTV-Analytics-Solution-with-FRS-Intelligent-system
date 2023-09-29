import sys

import numpy as np
import os
import face_recognition
import cv2
import test_2
import mailer

def start_record():
    callFlag = False

    path = 'images'
    images = []
    personName = []
    personAge = []
    personAddress = []
    myList = os.listdir(path)
    print(myList)

    for cu_img in myList:
        current_Img = cv2.imread(f'{path}/{cu_img}')
        images.append(current_Img)
        personName.append(os.path.splitext(cu_img)[0])


    print(personName)


    def faceEncodings(images):
        encodeList = []
        for img in images:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            encode = face_recognition.face_encodings(img)[0]
            encodeList.append(encode)
        return encodeList


    encodeListKnown = faceEncodings(images)
    print("All Encodings Completed!!!!")

    cap = cv2.VideoCapture(0)
    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))
    size = (frame_width, frame_height)
    result = cv2.VideoWriter('filename.avi', cv2.VideoWriter_fourcc(*'MJPG'), 6, size)

    while (True):


        ret, frame = cap.read()
        faces = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result.write(frame)

        fac2esCurrentFrame = face_recognition.face_locations(faces)
        encodesCurrentFrame = face_recognition.face_encodings(faces, fac2esCurrentFrame)

        for encodeFace, faceLoc in zip(encodesCurrentFrame, fac2esCurrentFrame):
            matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
            faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)

            matchIndex = np.argmin(faceDis)

            if matches[matchIndex]:

                Detail = personName[matchIndex]
                PersonDetail = Detail.split(" ")
                # PersonDetail.append()
                name = 'Name: ' + PersonDetail[0]
                age = 'Age: ' + PersonDetail[1]
                address = 'Address: ' + PersonDetail[2]
                print(name)
                print(age)
                print(address)
                y1, x2, y2, x1 = faceLoc
                y1, x2, y2, x1 = y1 - 50, x2 + 50, y2 + 50, x1 - 50
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                # cv2.rectangle(frame, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
                cv2.putText(frame, name, (x2 + 6, y1 + 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
                cv2.putText(frame, age, (x2 + 6, y1 + 100), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
                cv2.putText(frame, address, (x2 + 6, y1 + 150), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)


            else:
                name = 'UNKNOWN'
                if(callFlag==False):
                    callFlag = True
                    cv2.imwrite("unknown.jpg", frame)
                    test_2.makeCall()
                    mailer.send_email()
                print(name)

                y1, x2, y2, x1 = faceLoc
                y1, x2, y2, x1 = y1 - 50, x2 + 50, y2 + 50, x1 - 50
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.rectangle(frame, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
                cv2.putText(frame, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)

        cv2.imshow("Live Video Stream", frame)
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            sys.exit()


start_record()

