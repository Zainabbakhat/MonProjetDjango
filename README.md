# E-STORE Application


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
