# PATTERN PYTHON FLASK


## List Endpoint in Postman

[![Run in Postman](https://run.pstmn.io/button.svg)](https://www.getpostman.com/collections/483c8e75f7c16e19232b)

## Installing PYENV + PYENV VIRTUALENV

Please follow the steps here:

* https://pypi.org/project/virtualenv/

## Requirements
- Python 3.6
- Git
- virtualenv

## Editor (IDE)
- Visual Studio Code (Recommended)
- Sublime 3

After installing one of those editors, please make sure that you install [EditorConfig](http://editorconfig.org/) plugin so that every user will use the same editor configuration for this project.

## Coding Syle Guide

[PEP 8 -- Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)

## Structure Project
```sh
project_name/
.... app/
........ config/
........ controller/
........ library/
........ middleware/
........ model/
........ __init__.py
........ logger.py
........ route.py
.... tests/
... .editorconfig
... .env.example
... .gitignore
... README.md
... requirements.txt
... run.py
```

## Step By Step
Open your Terminal :
```sh
$ git clone https://github.com/sobatdigital/api_pattern_flask_mvc.git
$ cd project_name
$ virtualenv -p python3.6 env
$ source env/bin/activate
$ pip install -r requirements.txt
$ python run.py

Open postman and GET http://localhost:9001
```
Dont forget to Copy file .env.example to .env and change the values

## Who do I talk to? ##

If you have any questions, don't hesitate to ask us in  <sobatdigital.id@gmail.com>


**send email sobatdigital.id@gmail.com**
