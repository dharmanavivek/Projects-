import face_recognition
import cv2
import numpy as np
import csv
import os
from datetime import datetime
video_capture=cv2.VideoCapture(0)
karunakar_image=face_recognition.load_image_file("photos/karunakar.jpg")
karunakar_encoding =face_recognition.face_encodings(karunakar_image)[0]

karthik_image=face_recognition.load_image_file("photos/karthik.jpg")
karthik_encoding =face_recognition.face_encodings(karthik_image)[0]

vivek_image=face_recognition.load_image_file("photos/vivek.jpg")
vivek_encoding =face_recognition.face_encodings(vivek_image)[0]

know_face_encoding=[
karunakar_encoding,
karthik_encoding,
vivek_encoding
]
know_faces_names=[
"karunakar",
"karthik",
"vivek"]
students=know_faces_names.copy()

face_location=[]
face_encoding=[]
face_names=[]
s=True 

now =datetime.now()
current_date=now.strftime("%Y-%m-%d")

f=open(current_date+'.csv','w+',newline='')
lnwriter =csv.writer(f)
while True:
	_,frame =video_capture.read()
	small_frame=cv2.resize(frame,(0,0),fx=0.25,fy=0.25)
	rgb_small_frame=small_frame[:,:,::-1]
	if s:
		face_locations =face_recognition.face_locations(rgb_small_frame)
		face_encodings =face_recognition.face_encodings(rgb_small_frame,face_locations)
		face_names=[]
		for face_encoding in face_encodings:
			matches = face_recognition.compare_faces(know_face_encoding,face_encoding)
			name=""
			face_distance=face_recognition.face_distance(know_face_encoding,face_encoding)
			best_match_index=np.argmin(face_distance)
			if matches[best_match_index]:
				name=know_faces_names[best_match_index]

			face_names.append(name)
			if name in know_faces_names:
				if name in students:
					students.remove(name)
					print(students)
					current_time=now.strftime("%H-%M-%S")
					lnwriter.writerow([name,current_time])
	cv2.imshow("attendance system",frame)
	if cv2.waitKey(1) & 0xFF ==ord('q'):
		break

video_capture.release()
cv2.destroyALLWindows()
f.close()

