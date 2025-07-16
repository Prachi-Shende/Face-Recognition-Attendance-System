# Face-Recognition-Attendance-System

An AI-powered real-time attendance system using face recognition, Firebase Realtime Database, and Cloudinary for image storage.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)  
![OpenCV](https://img.shields.io/badge/OpenCV-FaceDetection-success)

---

Real-time webcam face detection, automatic attendance logging to Firebase, and student photo display from Cloudinary.  

---

##  Features

* Real-time face detection using webcam  
* Face recognition using `face_recognition` encodings  
* Cloud image storage and access using Cloudinary  
* Realtime attendance logging with Firebase Realtime Database  
* Custom UI overlay built with OpenCV and `cvzone`  
* Displays student name, year, attendance count, and last seen time  

---

##  Project Structure

FaceRecognitionProject/  
├── Images/ — Student images  
├── Resources/ — UI background and mode screens  
│   └── Modes/  
├── EncodeFile.p — Serialized face encodings  
├── serviceAccountKey.json — Firebase credentials (do not commit this)  
├── cloudinary_config.py — Cloudinary setup  
├── encode_faces.py — Encode and upload student data  
├── main.py — Real-time attendance system  
├── .gitignore  
└── README.md  

---

##  Tech Stack

| Technology         | Purpose                                    |
|--------------------|--------------------------------------------|
| Python 3.8+        | Programming language                       |
| OpenCV             | Image processing and webcam access         |
| face_recognition   | Face encoding and comparison               |
| Firebase Admin SDK | Realtime database to store attendance logs |
| Cloudinary         | Uploading and serving student face images  |
| cvzone             | Drawing UI components on frames            |

---

##  Setup Instructions

**1. Clone the repository**  
Run: `git clone https://github.com/your-username/Face-Recognition-Attendance-System.git`  
Then: `cd Face-Recognition-Attendance-System`

**2. Install dependencies**  
Run: `pip install -r requirements.txt`  
Key dependencies: opencv-python, face_recognition, firebase-admin, cvzone, cloudinary, numpy

**3. Set up Firebase**  
Go to [https://console.firebase.google.com/](https://console.firebase.google.com/)  
Create a new project and navigate to Project Settings → Service Accounts  
Generate a new private key and download `serviceAccountKey.json`  
Place it in the root directory  
Make sure to add it to `.gitignore`

**4. Set up Cloudinary**  
Create an account at [https://cloudinary.com/](https://cloudinary.com/)  
Create a file named `cloudinary_config.py` with:  
`import cloudinary`  
`cloudinary.config(cloud_name="your_cloud_name", api_key="your_api_key", api_secret="your_api_secret")`  
Replace with your actual credentials

---

##  Running the System

**Step 1: Encode student faces and upload to Firebase + Cloudinary**  
Run: `python encode_faces.py`  
This will:  
* Read images from `Images/`  
* Encode faces  
* Upload to Cloudinary  
* Store data in Firebase  
* Save local encodings in `EncodeFile.p`

**Step 2: Start real-time attendance**  
Run: `python main.py`  
This will:  
* Open webcam  
* Detect and recognize faces  
* Display UI overlay  
* Update Firebase attendance logs

---

##  Firebase Database Format

"Students": {  
&nbsp;&nbsp;"1": {  
&nbsp;&nbsp;&nbsp;&nbsp;"name": "Prachi Shende",  
&nbsp;&nbsp;&nbsp;&nbsp;"major": "Computer Engineering",  
&nbsp;&nbsp;&nbsp;&nbsp;"starting_year": 2017,  
&nbsp;&nbsp;&nbsp;&nbsp;"total_attendance": 10,  
&nbsp;&nbsp;&nbsp;&nbsp;"standing": "G",  
&nbsp;&nbsp;&nbsp;&nbsp;"year": 4,  
&nbsp;&nbsp;&nbsp;&nbsp;"last_attendance_time": "2020-06-26 00:54:34",  
&nbsp;&nbsp;&nbsp;&nbsp;"img_url": "https://..."  
&nbsp;&nbsp;},  
...  
}

---

##  Security Notes

* Do **not** commit your `serviceAccountKey.json` file  
* Keep your Cloudinary API keys private  
* Add to `.gitignore`:  
  `serviceAccountKey.json`  
  `*.p`

---

##  Credits

* OpenCV  
* face_recognition  
* Firebase Admin SDK  
* Cloudinary Python SDK  

---

##  Questions or Feedback?

Feel free to raise an issue or start a discussion in the repository if you have any questions or suggestions.

---
