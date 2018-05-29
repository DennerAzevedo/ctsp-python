#! /bin/bash

# asking for root access

[ $UID != 0 ] && exec sudo bash "$0" "$@"

# installing dependencies
apt install -y python3 python3-dev python3-venv mysql-client mysql-server default-libmysqlclient-dev

# configuring mysql user, and correcting a plugin problem that has been introduced in version 17.10
# if you're not using ubuntu 17.10, this will probably not change any configuration
echo -n "[root] root password for mysql:"
read -s rpw

# making needed changes to mysql
mysql -u root -p${rpw} -e "create database ctsp;create user 'ctsp'@'localhost' identified by '';grant all on ctsp.* to 'ctsp'@'localhost';update mysql.user set plugin='' where User='ctsp';flush privileges"

# cloning git project
git clone https://github.com/CTSP-Software/ctsp-python

# cd into cloned directory
cd ctsp-python/

# creating the virtual env
python3 -m venv ./venv

# activating virtual environment
source ./venv/bin/activate

#installing needed packages
pip install -U django mysqlclient