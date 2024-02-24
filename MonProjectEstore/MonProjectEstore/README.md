# E-epicier Application


---

### :gear: deployment

#### Crreate a new folder named `app` and open it with `Command Prompt`, `Terminal` or `VSCode`

> If you opened it with `VSCode` then open its terminal and do the following instructions to complete!

#### Download this application using `git`

```cmd
git clone https://github.com/Zainabbakhat/MonProjetDjango.git .
```

#### Create a virtuial environment

```cmd
python -m venv env
```

#### Activate the virtuial environment

```cmd
.\env\Scripts\activate
```

#### Install requirements

```cmd
pip install -r requirements.txt 
```

#### Editing the settings.py file

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'data',
        'USER': 'root',
        'PASSWORD': '', # PASSWORD is the root password (is empty if your root doesn't have a password)
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}
```
#### :warning: Create a database named `data` using `MySQL Workbench`, `MySQL Command Line` or `phpMyAdmin` :warning:

#### Create migrations

```cmd
python manage.py makemigrations
```

#### Migrate migrations

```cmd
python manage.py migrate
```

#### Create superuser

```cmd
python manage.py createsuperuser
```

#### Run the server

```cmd
python manage.py runserver
```

---
