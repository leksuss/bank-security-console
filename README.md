# Вank security console

This is Django-based application to show storage visitors in bank. It is use connection to external PostgreSQL database.

## Requirements

 - python3
 - `django`
 - `psycopg2-binary`
 - `python-dotenv`

## How to install

Get the source code of this repo:
```
git clone https://github.com/leksuss/dvmn.git
```

Go to this script:
```
cd dvmn/django-orm-watching-storage
```

Then install dependencies:
```
# If you would like to install dependencies inside virtual environment, you should create it first.
pip3 install -r requirements.txt
```

## How to setup

This app uses PostgreSQL database, so you should fill connection settings in `project/.env` file. You can use `project/.env_example` as template, like this:
```
cp project/.env_example project/.env
```

## How to use

Run script without arguments like this:
```
python3 main.py
```

After that open webpage `127.0.0.1:8000` in your browser.
