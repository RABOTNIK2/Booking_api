<h1 align='center'>API Центра принятия жалоб</h1>

Проект представляет собой центр принятия жалоб сделанный с использованием технологии Django Rest Framework. В проекте реализован весь CRUD, авторизация(использовалась библиотека djoser), дополнительные @action под тематику проекта 

### Тестирование
* Тестирование создания пользователя.
* Тестирование авторизации.
* Тестирование вывода всех жалоб.


### API Endpoint

#### User

* **/auth/users/** (Регистрация пользователя)
* **/auth/token/login/** (Авторизация пользователя)
* **/api/users/logout/** (Выход пользователя)
* **/api/users/me/** (Чтение пользователя GET, Редактирование пользователя POST, Удаление пользователя DELETE)
* **/complain_api/user/get_complains/** (Получение всех обращений POST)
  

#### Complains

* **/complain_api/complain/** (Вывод всех жалоб, 'GET')
* **/complain_api/complain/** (Добавление жалобы, 'POST')
* **/complain_api/complain/pk/** (Чтение жалобы, 'GET')
* **/complain_api/complain/pk/** (Редактирование жалобы, 'PUT')
* **/complain_api/complain/pk/** (Удаление жалобы, 'DELETE')


#### Category

* **/complain_api/category/** (Вывод всех категорий жалоб, 'GET')
* **/complain_api/category/** (Добавление категории, 'POST')
* **/complain_api/category/pk/** (Чтение категории, 'GET')
* **/complain_api/category/pk/** (Редактирование категории, 'PUT')
* **/complain_api/category/pk/** (Удаление категории, 'DELETE')


#### Answer

* **/complain_api/answer/** (Вывод всех ответов, 'GET')
* **/complain_api/answer/** (Добавление ответа, 'POST')
* **/complain_api/answer/pk/** (Чтение ответа, 'GET')
* **/complain_api/answer/pk/** (Редактирование заказа, 'PUT')
* **/complain_api/answer/pk/** (Удаление заказа, 'DELETE')


### Install 

    pip install -r req.txt

### Usage

    python manage.py test

### License

  Этот проект лицензирован под MIT License.


    

