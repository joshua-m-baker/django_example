# Rent-Prop-Server
Back End and Databse

# Setup
- Create a virtual environment
    - `mkdir ~/.envs`
    - `python3 -m venv ~/.envs/rentprop`
    - `source ~/.envs/rentprop/bin/activate`
- Install dependencies 
    - `pip install requirements.txt`

# Installation 
From Django recommended installation
Python version: 3.8
Django Version: 3.1.1

- python 3.8 installation 
    - `$ sudo apt install python3.8 python3.8-dev python3.8-distutils python3.8-venv`
- Create venv 
    - `mkdir ~/.envs`
    - `python3 -m venv ~/.envs/rentprop`
    - `source ~/.envs/rentprop/bin/activate`
- `pip install wheel` 
- Install mysql dev headers 
    - `sudo apt-get install python3-dev default-libmysqlclient-dev build-essential`
    - https://pypi.org/project/mysqlclient/
- `pip install mysqlclient`
- `pip install Django`

- `django-admin startproject rent_now`
- `pip install djangorestframework`
- `pip install markdown`
- `pip install django-filter`
- `cd rent_now`
- `django-admin startapp api`
- `python manage.py migrate`
