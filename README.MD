# Куда пойти
интерактивная карта Москвы с местами отдыха с подробными описаниями

### Что необходимо
1. Python3 должен быть уже установлен. 
2. Рекомендуется использовать [virtualenv/venv](https://docs.python.org/3/library/venv.html) для изоляции проекта.
4. Затем используйте pip (или pip3, есть конфликт с Python2) для установки зависимостей:
```python
pip install -r requirements.txt
```
4. Создайте файл `.env` и пропишите в нем переменные окружения:
- `SECRET_KEY` - [секретный ключ Django](https://docs.djangoproject.com/en/4.0/ref/settings/#secret-key);
- `DEBUG` - [флаг включения дебаг-режима](https://docs.djangoproject.com/en/4.0/ref/settings/#debug);
- `ALLOWED_HOSTS` - [список допустимых хостов/доменов](https://docs.djangoproject.com/en/4.0/ref/settings/#allowed-hosts).
5. Проведите миграцию командой: 
```python
python manage.py migrate
```
6. Cоздайте суперпользователя командой:
```python
python manage.py createsuperuser
```
### Как запустить
Запустите сервер на локальной машине командой:
```python
python manage.py runserver
```
После чего по адресу http://127.0.0.1:8000/ будет доступен сайт, а по адресу http://127.0.0.1:8000/admin - административная панель.

Пример работающего сайта можно посмотреть [тут](https://949027.pythonanywhere.com/).
### Как добавить новое место
1 вариант - в административной панеле, заполнив данные и добавив изображения (можно сортировать их перетаскивая мышью);

2 вариант - автоматически, командой:
```python
python manage.py load_place {url}
``` 
где `url` - ссылка на JSON-файл с содержимым вида:
```
{
    "title": "Название локации",
    "imgs": [
        "https://images.com/img1.jpg",
        "https://images.com/img2.jpg",
    ],
    "description_short": "Краткое описание (текст)",
    "description_long": "Подробное описание (HTML)",
    "coordinates": {
        "lng": "00.000000",        
        "lat": "00.000000"
    }
}
```
