vngo
====

<i>Free software for NGO</i>

VNGO is a free software for NGO project done by Víctor Arcas Ríos under the <b>GPL license</b>
You are free to download, use and do your own version of this project <u>as long as</ul> you still doing it under <b>GPL license</b>


<h1>INSTALLATION MANUAL</h1>

<h3> INSTALL DJANGO (Ubuntu 14.04) </h3>
<ol>
<li>Install Pip
<code>sudo apt-get install python-pip</code></li>
<li>Install Django
<code>sudo pip install Django==1.7.1</code></li>
</ol>

<h3>Install MySQLdb python driver (if you don't have it yet)</h3>
<code>sudo apt-get install python-mysqldb</code>

<h3>Install VNGO and setup its configuration</h3>
<ol>
<li>Clone or download and unzip vngo git repository</li>
<li>Enter the new vngo folder</li>
<li>Open <i>vngo/settings.py</i> and set database params to aim to your MySQL server.
You should only change user and password param values to the ones of your server.
The param names are meaningful</li>
<li>Create an empty database named <b>vngo</b>. You can change the aimed database in <i>settings.py</i> if you want to give it another name</li>
<li>Apply migrations before run the application (it create all the needed tables in the database)
<code>python manage.py migrate</code></li>
<li>Run the server and finally see vngo running
<code>python manage.py runserver</code></li>
<p>Now you can see it at <b>localhost:8000</b> (default port is 8000, 
you can specify at the end of runserver command if you preefer another port)</p>


<h1>USER MANUAL</h1>

<h3>ADMIN PANEL:</h3>
<p>Admin panel is situated at <b>localhost:8000/admin</b></p>
<p>You need a user-password combo to enter it. Use the next command to get one:</p>
<code>python manage.py createsuperuser</code>
