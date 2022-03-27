### Первичная установка
`pip install Django`  
`django-admin startproject news  `  
`python manage.py startapp app_news  `  
`pip install djangorestframework ` 
`pip install django-filter  `  
`pip freeze > requirements.txt  `  
 
`python manage.py makemigrations`  
`python manage.py migrate`  

#### Наполнение базы данных
- Через fixtures (здесь, но не все данные сразу)  
`python manage.py loaddata initial_data.json`
- Через админку (минимально)
- Через пустую миграцию и параметр operations

python manage.py createsuperuser  
denis 1234  

После импорта фикстур можно создать пароли через тесты.  
https://stackoverflow.com/questions/8017204/users-in-initial-data-fixture  
#### Локализация
Должна быть установлена gettext  
https://mlocati.github.io/articles/gettext-iconv-windows.html  
`python manage.py  makemessages -l ru`  
`python manage.py  makemessages -l en`  
`python manage.py  compilemessages`
