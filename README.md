Simplify this code Run :

<p> create a virtual env uisng this commands : python -m venv name of your virtual env file  <br/> And smiply active this command name of your virtual env file\Scripts\activate </p>
<p>Install requirements.txt file using this command : pip install -r requirements.txt
 </p>

 <p> connect your dtabase using any database  use .env.local File to setup database :
DEBUG=True
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=your_db_host
DB_PORT=your_db_port
 </p>

 <p>then simply migrate your database using this commands : python manage.py migrate <br/> or <br/> using you are python3 then use this command python3 manage.py migrate </p>
 <p> And also to view django admin panel createsuperuser using this command : python manage.py createsuperuser  simply set username and password and   url(http://127.0.0.1:8000/admin) 
 to login page and view data.
 </p>
 
<p>finally : run your server using this commands : python manage.py runserver or using python3</p>
 <p>Views any api then use this : url(http://127.0.0.1:8000/api)</p>

