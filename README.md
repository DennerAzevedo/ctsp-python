# CTSP - Cloud Tool For Scrum Practitioners

CTSP is a open source software to help you manage your team software development based on Scrum principles of agile development. Different from other softwares available on the market, CTSP comes configurates out of the box.

## Getting Started
### Prerequisites (dependencies)

The project is mainly made to run on Linux. The system dependencies for this project are the following packages:

* python3
* python3-dev
* mysql-client
* mysql-server
* libmysqlclient-dev
* python3-venv (python dependencies will be treated later)

You can run the **system_dependencies.sh** script inside the project folder to install it automatically for you.

After installing those dependencies, clone the project and cd into this folder with the following command:
```
cd ctsp-python
```
Then create a virtual environment with the following command:
```
python3 -m venv ./venv
```
Now activate your virtual environment with the following command:
```
source venv/bin/activate
```
Now install the python3 dependencies running the following command:
```
pip install -U django mysqlclient
```
Now you have your setup to build the project. Continue from this part.

### Having the server up

Inside the ctsp-python directory, run the following command to enter the project directory:
```
cd ctsp-python/project/
```
Inside the directory you're right now you should find a manage.py script. Now run this script with python3 and pass the runserver argument with the following command (your python virtual environment should be activated):
```
python3 manage.py runserver
```
Now you have a local server running on port 8000, you can then run CTSP locally writing on http://localhost:8000/ctsp

### Having the functionalities
CTSP utilizes a MySQL. So, for development and testing purposes, you are going to need a MySQL client and server up and running on your system.
Follow this tutorial by Jeremy Morris on how to set up your Django install to utilize MySQL databases instead of SQLite:

* [Installing MySQL to Django](https://www.digitalocean.com/community/tutorials/how-to-create-a-django-app-and-connect-it-to-a-database) - During the tutorial, change *python* for *python3*, and the database name to *ctsp*.
