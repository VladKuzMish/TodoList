## Автор:
##### Кузьмин Владислав (email - Sindbad1613@mail.ru)
## Описание:
##### TodoLIst - это REST API проект в рамках тестового задания, с его помощью можно смотреть, создавать и удалять записи
## Как запустить проект:
#### Скачиваем репозиторий проекта:
``` git clone git@github.com:VladKuzMish/TodoList.git```
#### Создаем виртуальное окружение:
``` python -m venv venv```
##### При необходимости указываем версионность инициализатора:
```py -3.10 -m venv venv```
#### Активируем виртуальное окружение: 
```source venv/Scripts/activate```
#### Устанавливаем зависимости из файла requirements.txt:
```python -m pip install --upgrade pip```

```pip install -r requirements.txt```
#### Выполняем миграции:

```python manage.py migrate```
#### Запускаем проект:

```python manage.py runserver```
