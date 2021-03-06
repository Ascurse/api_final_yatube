# api_yatube
Api для социальной сети yatube https://github.com/Ascurse/Yatube_network.
#### Технологии
- Python 3.7.0
- Django 2.2.16
- Django REST framework 3.12.4
- Simple JWT 4.7.2


### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/Ascurse/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

#### Обратиться с проекту можно по адресу:
http://127.0.0.1:8000
#### Доступ к документации:
http://127.0.0.1:8000/redoc
