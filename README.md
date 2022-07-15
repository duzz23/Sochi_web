Порядок установки Клонировать репозиторий к себе, установить и активировать виртуальное окружение:

python -m venv venv
venv\Scripts\activate.bat 
git clone https://github.com....
перейти в папку проекта, установить зависимости:

cd sending
pip install -r requirements.txt
запустить и применить миграции:

python manage.py makemigrations
python manage.py migrate
Запустить проект:

python manage.py runserver


Данный сайт реализован на Wagtail CMS
Имя: admin
Пароль: admin

Задача:
Переделать сайт с динамичными блоками, для удобства администрирования: 
Header menu, мероприятия, спонсоры, социальные сети, спикеры, организаторы, все это динамические блоки. 
Посторена структура блоков с "Спикерами" и "Мероприятей" Many to Many
Реализовано время проведения меропрятей и возможности зарегистрироваться в актуальное время. 


This site is implemented on Wagtail CMS
Name: admin
Password: admin

A task:
Redesign the site with dynamic blocks for ease of administration:
Header menu, events, sponsors, social networks, speakers, organizers, all these are dynamic blocks.
The structure of blocks with "Speakers" and "Events" Many to Many has been built
Implemented the time of the events and the possibility to register at the current time.
