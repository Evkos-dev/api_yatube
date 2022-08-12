# API социальной сети YaTube
### Описание проекта
Проект создан в рамках учебного курса Яндекс.Практикум.
В данном проекте реализованы следующие функции:

- Посты (Получить список всех постов или отдельного поста по id, создать новый пост, редактировать или удалить пост по id для авторизованного пользователя)

- Коментарии (Получить список всех комментариев поста, создать, обновить или удалить комментарий поста по id)

- JWT-токен (Получение или обновление токена)

- Подписки (Получить список всех подписчиков, создать подписку)

- Группы (Получить список всех групп или информацию об отдельной)

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
