<b>Django Online Examination Project</b>
===============
Project Created By,
 

Name |
-----|
Raj Rao
Kashish Gandhi
Harsh N Patel  
Harsh S Patel
					
<b>Requirements</b>
------------
django-model-utils

Pillow


<b>Installation</b>
------------
- This project requires postgre SQL as Database and pgAdmin as management tool. 
- Create Database using pgAdmin according to <b>setting.py</b>
- Run this project in virtual environment. 


Install necessary packages.
```sh
pip install -r requirement.txt
```
Migrate models.
```sh
python manage.py makemigrations
pyhton manage.py migrate
```
Set Django-admin User.
```sh
python manage.py createsuperuser
```
Run server.
```sh 
python manage.py runserver 
```







