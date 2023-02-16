# Вank security console

This is Django-based application to show storage visitors in bank. It is use connection to external PostgreSQL database.

## Requirements

 - python3
 - `django`
 - `psycopg2-binary`
 - `environs`

## How to install

Get the source code of this repo:
```
git clone https://github.com/leksuss/bank-security-console.git
```

Go to this script:
```
cd bank-security-console
```

Python3 should be already installed. Then use pip (or pip3, if there is a conflict with Python2) to install dependencies:
```
# If you would like to install dependencies inside virtual environment, you should create it first.
pip3 install -r requirements.txt
```

## How to setup

This app uses PostgreSQL database, so you should fill connection settings in `project/.env` file and other settings. You can use `project/.env_example` as template, like this:
```
cp project/.env_example project/.env
vim project/.env
```

The variables starting at `DB_` represent PostgreSQL connection settings. You also need to generate `SECRET_KEY` like this (Django method `get_random_secret_key` may be [insecure](https://github.com/django/django/pull/13183)):
```
python3 -c 'import secrets; print(secrets.token_hex(100))'
```


## How to use

Run server without arguments like this:
```
python3 manage.py runserver 127.0.0.1:8000
```

After that open webpage `127.0.0.1:8000` in your browser.


## Project Goals

The code is written for educational purposes on online-course for web-developers dvmn.org.
