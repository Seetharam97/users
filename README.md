# users
users management by django backend only

Step:1

create the mysql database 
**users**


Step:2

create or activate the vitualenvironment
if create:
  type the command: **virtualenv (virtualenv name)**
else activate:
  type the command: **. (virtualenv name)/bin/activate

then..

**pip3 install -r requirement.txt**

Step: 3
 Configure the database in settings.py

Step: 4

To ready to migrate the tables
**python3 manage.py makemigrations**

To migrate the tables
**python3 manage.py migrate**

finally run the code in locally
**python3 manage.py runserver**
