import os
import cv2
import face_recognition
import pickle
import cloudinary
import cloudinary.uploader
import cloudinary_config
import firebase_admin
from firebase_admin import credentials, db

# Firebase setup
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    "databaseURL": "https://faceattendancerealtime-bae9f-default-rtdb.firebaseio.com/"
})

# Upload images and encode faces
folderPath = 'Images'
pathList = os.listdir(folderPath)
imgList = []
studentIds = []
imgUrls = []

for path in pathList:
    filePath = os.path.join(folderPath, path)
    img = cv2.imread(filePath)
    imgList.append(img)

    student_id = os.path.splitext(path)[0]
    studentIds.append(student_id)

    # Upload to Cloudinary
    result = cloudinary.uploader.upload(filePath, folder="attendance")
    imgUrls.append(result['secure_url'])


# Encode faces
def findEncodings(imagesList):
    encodeList = []
    for img in imagesList:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList


encodeListKnown = findEncodings(imgList)
encodeListKnownWithIds = [encodeListKnown, studentIds]
pickle.dump(encodeListKnownWithIds, open("EncodeFile.p", 'wb'))

# Save image URLs in DB
ref = db.reference('Students')
for sid, url in zip(studentIds, imgUrls):
    ref.child(sid).update({"img_url": url})

print("Encoding Complete and Uploaded to Cloudinary")
