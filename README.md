# Сайт с рецептами

Это веб-приложение предназначено для хранения, просмотра и добавления рецептов различных блюд. Пользователи могут зарегистрироваться, войти в свой профиль, добавлять новые рецепты, редактировать и удалять их, а также просматривать рецепты других пользователей.

## Установка и запуск

1. Установите Python и Django.
2. Клонируйте репозиторий с помощью команды `git clone`.
3. Перейдите в каталог проекта `cd recipe_website`.
4. Установите зависимости, выполнив команду `pip install -r requirements.txt`.
5. Создайте базу данных, выполнив команду `python manage.py migrate`.
6. Создайте административного пользователя с помощью команды `python manage.py createsuperuser`.
7. Запустите сервер разработки с помощью команды `python manage.py runserver`.
8. Откройте браузер и перейдите по адресу `http://127.0.0.1:8000/`.

## Использование

### Главная страница

На главной странице отображаются случайные рецепты из базы данных. Пользователи могут просматривать рецепты, переходя на страницы деталей каждого рецепта.

### Регистрация и аутентификация

Пользователи могут зарегистрироваться на сайте, перейдя по ссылке "Регистрация". После регистрации они могут войти на сайт, используя форму входа.

### Профиль пользователя

После аутентификации пользователи могут управлять своим профилем, изменяя свое имя пользователя через страницу "Изменить имя пользователя" в верхнем меню.

### Добавление рецептов

Зарегистрированные пользователи могут добавлять новые рецепты, перейдя на страницу "Добавить рецепт" в верхнем меню. Они могут указать название, описание, ингредиенты, шаги приготовления, время приготовления и прикрепить изображение к рецепту.

### Поиск рецептов

На странице поиска пользователи могут искать рецепты по названию. 

### Управление рецептами

Пользователи могут редактировать и удалять свои рецепты через страницы редактирования и деталей каждого рецепта. Они также могут удалять рецепты, если они являются их авторами.

## Технологии

- Django: фреймворк для веб-разработки на языке Python.
- HTML/CSS: языки разметки и стилей для создания внешнего вида сайта.
- JavaScript: язык программирования для создания интерактивных элементов на веб-страницах.

## Автор

Этот проект разработал [VictoriaKeshishian] в рамках своего проекта выпускной работы.

