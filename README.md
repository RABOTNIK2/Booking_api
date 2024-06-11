<h1 align='center'>API Приложения по бронированию номеров</h1>

Проект представляет собой приложения по бронированию номеров сделанный с использованием технологии Django Rest Framework. В проекте реализован весь CRUD, авторизация(использовалась библиотека djoser), дополнительные @action под тематику проекта 

### Тестирование
* Тестирование добавления брони.
* Тестирование добавления в избранное .
* Тестирование удаления из избранного.
* Тестирование добавления отзыва.


### API Endpoint

#### User

* **/auth/users/** (Регистрация пользователя)
* **/auth/token/login/** (Авторизация пользователя)
* **/api/users/logout/** (Выход пользователя)
* **/api/users/me/** (Чтение пользователя GET, Редактирование пользователя POST, Удаление пользователя DELETE)
* **/booking_api/user/add_to_fav/** (Добавление в избранное PUT)
* **/booking_api/user/del_from_fav/** (Удаление из избранного PUT)
  

#### Hotel

* **/booking_api/hotel/** (Вывод всех  отелей, 'GET')
* **/booking_api/hotel/** (Добавление отеля, 'POST')
* **/booking_api/hotel/pk/** (Чтение отеля, 'GET')
* **/booking_api/hotel/pk/** (Редактирование отеля, 'PUT')
* **/booking_api/hotel/pk/** (Удаление отеля, 'DELETE')


#### Booking

* **/booking_api/bookin/** (Вывод всех записей, 'GET')
* **/booking_api/bookin/** (Добавление брони, 'POST')
* **/booking_api/bookin/pk/** (Чтение брони, 'GET')
* **/booking_api/bookin/pk/** (Редактирование брони, 'PUT')
* **/booking_api/bookin/pk/** (Удаление брони, 'DELETE')


#### Review

* **/booking_api/review/** (Вывод всех отзывов, 'GET')
* **/booking_api/review/** (Добавление отзыва, 'POST')
* **/booking_api/review/pk/** (Чтение отзыва, 'GET')
* **/booking_api/review/pk/** (Редактирование отзыва, 'PUT')
* **/booking_api/review/pk/** (Удаление отзыва, 'DELETE')


### Install 

    pip install -r req.txt

### Usage

    python manage.py test

### License

  Этот проект лицензирован под MIT License.


    

