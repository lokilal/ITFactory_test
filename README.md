##### Тестовое задание для компании ITFactory_test
Создать простое API для мобильного приложения, в котором полевой сотрудник
заказчика будет выполнять визиты в магазины.
##### Реализация
Стек: Django == 3.2, Django-rest-framework, PostgreSQL 
Проект завернут в docker-compose, чтобы запустить его откройте папку `infra` и введите команду в консоль `sudo docker-compose up --build -d`. Затем откройте страницу http://localhost
Проекте присутствуют фикстуры, чтобы загрузить их введите команду в консоль `sudo docker-compose exec web python manage.py loaddata fixtures.json`
Данные от суперпользователя: 
- login - admin 
- password - admin

Существуют два эндпоинта: 
- http://localhost/api/v1/worker/?phone_number=<int>
- http://localhost/api/v1/visiting/?phone_number=<int>

С помощью первого можно получить список торговых точек, привязанных к опеределенному номеру. Чтобы указать номер, необходимо передать его в строке запроса, например, http://localhost/api/v1/worker/?phone_number=12345
С помощью второго можно создать посещение человека в торговую точку, к которой он привязан. Номер передается тоже в строке запроса, например, http://localhost/api/v1/visiting/visiting/?phone_number=12345. 
Параметры, которые принимает второй: 
- latitude - float 
- longitude - float 
- pk( Торговой точки) - int

Возвращает время и pk посещения. 
