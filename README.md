# API социальной сети YaTube
### Описание проекта
Проект создан в рамках учебного курса Яндекс.Практикум.
В данном проекте реализованы следующие функции:

- Посты (Получить список всех постов или отдельного поста по id, создать новый пост, редактировать или удалить пост по id для авторизованного пользователя)

  ###### Пример GET запроса:
  `"/api/v1/posts/"`
  ###### Пример ответа:
  ```
  {
  "count": 123,
  "next": "http://api.example.org/accounts/?offset=400&limit=100",
  "previous": "http://api.example.org/accounts/?offset=200&limit=100",
  "results": [
    {
      "id": 0,
      "author": "string",
      "text": "string",
      "pub_date": "2021-10-14T20:41:29.648Z",
      "image": "string",
      "group": 0
    }
    ]
  }
  ```

- Коментарии (Получить список всех комментариев поста, создать, обновить или удалить комментарий поста по id)

  ###### Пример POST запроса:
  `/api/v1/posts/{post_id}/comments/`
  ```
  {
  "text": "string"
  }
  ```
  ###### Пример ответа:
  ```
  {
  "id": 0,
  "author": "string",
  "text": "string",
  "created": "2019-08-24T14:15:22Z",
  "post": 0
  }
  ```
- JWT-токен (Получение или обновление токена)

- Подписки (Получить список всех подписчиков, создать подписку)

- Группы (Получить список всех групп или информацию об отдельной)

### Стек технологий
- Python 3.7
- pytest 6.2
- Django 2.2
- Django Rest Framework 3.12
- Simple-JWT 4.7
- SQLite3

### Документация к проекту
Документация для API после установки доступна по адресу `/redoc/`.

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

`git clone https://github.com/Evkos-dev/api_final_yatube.git`

`cd api_final_yatube`

Cоздать и активировать виртуальное окружение:

`python3 -m venv venv`

`source venv/Scripts/activate`

Установить зависимости из файла requirements.txt:

`python -m pip install --upgrade pip`

`pip install -r requirements.txt`

Выполнить миграции:

`python3 manage.py migrate`

Запустить проект:

`python3 manage.py runserver`

### Об авторе
<<<<<<< HEAD
Я студент Яндекс.Практикума, обучаюсь Backend разработке на Python. Этот проект - учебный, где я реализовывал API для социальной сети с помощью Django Rest Framework.
=======
Я студент Яндекс.Практикума, обучаюсь Backend разработке на Python. Этот проект - учебный, где я реализовывал API для социальной сети с помощью Django Rest Framework.
>>>>>>> 9908d469b19110061037d39281f24b7d72267275
