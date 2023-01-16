# Hospital Management System
Hospital Management System using SQLite, Django and Bootstrap

## Need to work on:
Ability to accept the appointment by the doctor to acknowledge the patient that their appointment has been approved.
User should not be allowed to register if he/she tries to provide the already registered email ID.
The password should be encrypted and the password field shouldn't be displayed in the admin panel.
mplementation of pagination for all the list view across the application.
Implementation of export button in admin module to export all details to an excel sheet.



## Languages and Technologies used
1. HTML5/CSS3
2. JavaScript (to create dynamically updating content)
3. Bootstrap (An HTML, CSS, and JS library)
4. Django .

- Download This Project Zip Folder and Extract it
- Move to project folder in Terminal. Then run following Commands :
```
py manage.py makemigrations
py manage.py migrate
py manage.py runserver
```
- Now enter following URL in Your Browser Installed On Your Pc
```
http://127.0.0.1:8000/



-------------------------------------------------------------------------------------------------------------------------------
FEATURES
-------------------------------------------------------------------------------------------------------------------------------

Overview (Auth)
- User's can register directly on the app or can login using social network. 
- After authenticated user's will need to complete their profile (choose their doctor,writting their bio etc)
- If registered user is a doctor , then it will need first to create a profile and after the admin 
will need to upgrade the account from django administration.

Overview (Dashboard) 
- User's here can see their profile and basic things about their doctor profile. 
- Can create appointments. *(They can reserve dates from the date today and after 1 month,they can't select sunday or saturday)
- Can see avaiability. (Can select avaiabile date,see reserved appointments and convert them to excel)

Overview (Doctor Dashboard) 
- Can view the total number appointments reserved with him, number of appointments for each day.
- Can convert patients list into excel 
- Can convert upcoming appointments into excel 
- Can delete appointments 

Overview (Doctors) 
- It contains the models (Doctor, Appointment, Profile)

-------------------------------------------------------------------------------------------------------------------------------
USEFUL INFORMATION
-------------------------------------------------------------------------------------------------------------------------------


Running app  : python manage.py runserver 

 

-----------------------------
Login credentials for admin 
-----------------------------
USERNAME : admin
PASSWORD : admin 
-----------------------------
By :Rafeek mhajne.
