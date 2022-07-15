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

<img width="1280" alt="Снимок экрана 2022-07-15 в 12 06 14" src="https://user-images.githubusercontent.com/19858001/179221250-454b9c2c-2e26-46fd-bf64-a4a9d3fbb972.png">
<img width="1280" alt="Снимок экрана 2022-07-15 в 12 06 22" src="https://user-images.githubusercontent.com/19858001/179221267-37dd70fb-bef3-4a11-a7e6-5fdcdb9811a7.png">
<img width="1280" alt="Снимок экрана 2022-07-15 в 12 07 08" src="https://user-images.githubusercontent.com/19858001/179221273-93c6f849-a082-4ba5-99de-1878c448169e.png">
<img width="1280" alt="Снимок экрана 2022-07-15 в 15 05 48" src="https://user-images.githubusercontent.com/19858001/179221278-d833c10b-2db2-4758-bfa5-dd58b7c5b8ee.png">
<img width="1280" alt="Снимок экрана 2022-07-15 в 15 06 10" src="https://user-images.githubusercontent.com/19858001/179221280-66c895db-23a2-4a4c-934b-46072e36c1bb.png">
<img width="1280" alt="Снимок экрана 2022-07-15 в 15 06 28" src="https://user-images.githubusercontent.com/19858001/179221282-e17aedcb-4415-42b9-b2e2-d451b0a321ae.png">



