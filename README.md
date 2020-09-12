Сервис для хранения и подачи объявлений.
	
# Требования

Язык, технологии: Python, PostgreSQL, Django REST framework

Методы: получение списка объявлений, получение одного объявления, создание объявления.
Методы обрабатывают HTTP POST/GET запросы c телом, содержащим все необходимые параметры в JSON.


## Получение списка объявлений

Запрос: http://localhost:8000/api/v1/ads/

GET-Аргументы: page

Ответ: список объявлений (название объявления, ссылка на фото, цена)


## Создание объявления

Запрос: http://localhost:8000/api/v1/ads/

Ответ: id объявления, название объявления, цена, описание, время создания, дата редактирования


## Получение конкретного объявления

Запрос: http://localhost:8000/api/v1/ads/pk/

Ответ: id объявления, название объявления, цена, описание, ссылки на фото, время создания, дата редактирования


## Загрузка фото

Запрос: http://localhost:8000/api/v1/photo/

Ответ: ссылка на фото, id объявления
