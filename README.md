# Face recognition based attendance system 


### What is it? 🤔
Attendance System is a Web Application that lets the User gets his attendance marked by
utilising facial recognition. The User through this application can get his attendance marked
for numerous courses he has been added to. He can Register himself first and then log in to
his account. After that, he can contact the admin to get his profile updated. After that when
the admin sets up the user profile, the latter can mark his attendance by simply switching on
his camera, getting his photo clicked and submitting it. 
The application intends to serve as an efficient substitute for traditional attendance
systems. It can be used in Schools and University Institutions where attendance is considered
mandatory. 

### Vision of the Application 🚀
This Application currently serves the basic need of a Student of keeping his attendance record but has the ability with extra features added to act as a Student Portal where the Student can not only mark or view his attendance but can also see his Number of classes attend out of number of classes held. And get his attendance percentage. Get Notified if attendance gets below the required percentage. Can view his grades also and have the chat feature to directly contact to his teacher through the Web Application. 



### Face Recognition API 💻
For comparing and recognizing faces, I have used [Face Recognition API](https://pypi.org/project/face-recognition/) .
It simply compares the face of the person with the face of the person in the database.
The images get compared using the Face Recognition Api which recognizes and manipulates faces
from python or from the command line. It’s built using dlib’s stat-of-the-art face
recognition. 
This compares a list of face encodings against a candidate encoding to see if they match. It
returns a list of True/False values indicating which known_face_encodings match the face
encoding to check. 
It requires C++ and Cmake to be installed in the system.


### Tech Stack 📑
1. Django

Django has been used to handle the authentication and Database. I have made use of one of its
most powerful features the Automatic admin Interface where an admin can manage content on the
site.

2. Bootstrap

Bootstrap has been used as a frontend framework to build this fast and responsive site with its various helpful JavaScript plugins alongside HTML & CSS. 

3. Python

Python was chosen as the backend language. 

### Functionalities 

The Functionalities that can be performed by the admin are:
1. Adding and Updating Courses.
2. Adding and Updating Student/User Profile.
3. Viewing successfully marked attendance and Users Attendance History.

The Functionalities that can be performed by the User are:
1. Register and Login
2. Mark his Attendance
3. View his Attendance

### How to run it locally? 
1. Clone this repository in your local System.
2. Install Python 3.7+ in your system and make sure you have configured the environment variables.
    Test the environment variables by running the following command:
    ```
   python
   ```
   If it works, you can proceed further.

2. Install C++ compiler in the system and CMake. Do Make sure you have configured the environment variables.
    Test the environment variables by running the following command:
    ```
   g++
   ```
   If it works, you can proceed further.

3. Create a virtual environment by running the following command
   ```
   python -m venv env
   ```
   After the environment gets created you need to activate it.
    ```
    (source).\env\Scripts\activate
     ```
    Test the environment variables.
    If it works, you can proceed further.

4. Install the required packages by running the following command.
    ```
   pip install -r requirements.txt
   ```
   If it works, you can proceed further.

5. Add the environment variable into the system. Few important ones are `DEBUG`
    and the `Database` settings. 
   
6. Create migrations and migrate the database.
    ```
   python manage.py makemigrations
   python manage.py migrate
   ```
7. Create a superuser. Here you would need to enter the details of an admin.
    ```
   python manage.py createsuperuser
   ```
8. Run the server.
    ```
   python manage.py runserver
   ```
9.  That's it! You can enjoy now. 
 
### Link to the application
Check out the live demo:
https://oyster-app-poiwp.ondigitalocean.app/

Note: You would probably be needing to contact me to get your User profile updated. Feel Free
to do so. You can email me here : kajalmahato7677@gmail.com

### Link to the documentation
Check out the deatiled documentation of the Application:
https://drive.google.com/file/d/1kkM15j6sSH0J9lVR5ZT0wiiHNJrMFRIz/view?usp=sharing

Please do ⭐ the repository, if it helped you in anyway.
