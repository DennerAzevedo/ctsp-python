# CTSP - Cloud Tool For Scrum Practitioners

CTSP is a open source software to help you manage your team software development based on Scrum principles of agile development. Different from other softwares available on the market, CTSP comes configurates out of the box.

## Getting Started
### Prerequisites

The project is mainly made to run on Linux. The dependencies for this project are the following packages:

* python3
* python3-dev
* mysql-client
* mysql-server
* libmysqlclient-dev
* python3-venv

### Having the server up

First of all, clone the GitHub project into a local machine running:

```
git clone https://github.com/CTSP-Software/ctsp-python
```

Then you should run the commands:

```
cd ctsp-python/project/
```

Inside the directory you're right now you should find a manage.py script. Now run this script with python3 and pass the runserver argument.:

```
python3 manage.py runserver
```

Now you have a local server running on port 8000, you can then run CTSP locally writing on http://localhost:8000/ctsp

### Having the functionalities
CTSP utilizes a MySQL. So, for development and testing purposes, you are going to need a MySQL client and server up and running on your system.
Follow this tutorial by Jeremy Morris on how to set up your Django install to utilize MySQL databases instead of SQLite:

* [Installing MySQL to Django](https://www.digitalocean.com/community/tutorials/how-to-create-a-django-app-and-connect-it-to-a-database) - During the tutorial, change *python* for *python3*, and the database name to *ctsp*.
