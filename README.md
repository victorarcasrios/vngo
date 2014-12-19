vngo
====

Free software for NGO

#################################################################################################################################

VNGO is a free software for NGO project done by Víctor Arcas Ríos under the GPL license
You are free to download, use and do your own version of this project as long as you still doing it under GPL license

*********************************************************************************************************************************

INSTALLATION MANUAL
--------------------

## INSTALL DJANGO (Ubuntu 14.04) ##
1. Install Pip
# sudo apt-get install python-pip
2. Install Django
# sudo pip install Django==1.7.1

## Install MySQLdb python driver (if you don't have it yet) ##
# sudo apt-get install python-mysqldb

## Install VNGO and setup its configuration ##
1. Clone or download and unzip vngo git repository
2. Enter the new vngo folder
3. Open vngo/settings.py and set database params to aim to your MySQL server.
You should only change user and password param values to the ones of your server.
The param names are meaningful
4. Create an empty database named vngo. You can change the aimed database in settings.py if you want to give it another name
5. Apply migrations before run the application (it create all the needed tables in the database)
# python manage.py migrate
6. Run the server and finally see vngo running
# python manage.py runserver
Now you can see it at localhost:8000 (default port is 8000, 
you can specify at the end of runserver command if you preefer another port)

*********************************************************************************************************************************

USER MANUAL
-----------

1. ADMIN PANEL:
Admin panel is situated at localhost:8000/admin 
You need a user-password combo to enter it. Use the next command to get one:
# python manage.py createsuperuser
