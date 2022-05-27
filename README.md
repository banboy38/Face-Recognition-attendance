# Face recognition based attendance system


### What is it?
This application help teacher and student mark and view their attendance by applying 
face recognition technology.


### Face Recognition API
For comparing and recognizing faces, we use [Face Recognition API](https://pypi.org/project/face-recognition/)
It simply compares the face of the person with the face of the person in the database.
It requires C++ and Cmake to be installed in the system.


### Tech Stack
1. Django
2. Bootstrap
3. Python


### How to run it locally
1. Install Python 3.7+ in the system and make sure you have configured the environment variables.
    Test the environment variables by running the following command:
    ```
   python
   ```
   If it works, you can proceed further.

2. Install C++ compiler in the system and cmkae sure you have configured the environment variables.
    Test the environment variables by running the following command:
    ```
   g++
   ```
   If it works, you can proceed further.

3. Create a virtual environment and activate it.
    Test the environment variables by running the following command:
    ```
   pip install virtualenv
   virtualenv venv
   source venv/bin/activate
   ```
   If it works, you can proceed further.

4. Install the required packages.
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
7. Create a superuser.
    ```
   python manage.py createsuperuser
   ```
8. Run the server.
    ```
   python manage.py runserver
   ```
   
### How to run it on Server
Make any changes to the github repository it will trigger the build for the new 
commit and then the new application will be deployed on the server.



