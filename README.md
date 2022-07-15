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

<img width="1280" alt="Снимок экрана 2022-07-15 в 15 06 00" src="https://user-images.githubusercontent.com/19858001/179220834-7b642150-dde3-4d54-bf63-4c58dd60ea11.png">
<img width="1280" alt="Снимок экрана 2022-07-15 в 12 06 37" src="https://user-images.githubusercontent.com/19858001/179220842-494e79f6-b5f3-437d-9a2c-418267918d73.png">
<img width="1280" alt="Снимок экрана 2022-07-15 в 12 06 46" src="https://user-images.githubusercontent.com/19858001/179220859-72fc2758-f18d-460f-9df1-5b509cb5d0ae.png">
<img width="1280" alt="Снимок экрана 2022-07-15 в 15 06 10" src="https://user-images.githubusercontent.com/19858001/179220863-bfcd9907-404c-4606-8c62-88ae7bfdd763.png">
<img width="1280" alt="Снимок экрана 2022-07-15 в 12 07 08" src="https://user-images.githubusercontent.com/19858001/179220867-6b603d46-fb3f-4d44-9ffb-22d30313c5b0.png">
<img width="1280" alt="Снимок экрана 2022-07-15 в 12 06 22" src="https://user-images.githubusercontent.com/19858001/179220871-37481f99-124e-4371-b956-8c5a40eb8a41.png">
<img width="1280" alt="Снимок экрана 2022-07-15 в 15 05 48" src="https://user-images.githubusercontent.com/19858001/179220877-3d26d17d-a5f2-4219-aeee-46cd4eabf691.png">
<img width="1280" alt="Снимок экрана 2022-07-15 в 15 06 28" src="https://user-images.githubusercontent.com/19858001/179220883-d254f195-e72e-4918-9ca2-4767c9aed1ad.png">
<img width="1280" alt="Снимок экрана 2022-07-15 в 12 06 14" src="https://user-images.githubusercontent.com/19858001/179220884-7ca74350-862b-42f3-a6cd-c3b41dbc5f67.png">


