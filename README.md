# YaPr_Diplom

Описание заданий практического блока (вторая часть).

Работа с базой данных.

Инструкция по работе с SQL запросами:

1. Важно: перед обращением к БД требуется наполнить базу данными: создать заказы, курьеров. А также принять заказы в работу.

2. Подключаемся к серверу по SSH:
$ ssh 79e172fe-7b2d-441b-9085-bd2266701863@serverhub.praktikum-services.ru -p 4554

3. Подключаемся к БД. Пароль - smith:
psql -U morty -d scooter_rent

4. Обращаемся к БД:
Задание 1: SELECT c.login, COUNT(o."firstName") AS ordersindelivery FROM "Couriers" AS c LEFT JOIN "Orders" AS o ON c.ID = o."courierId" WHERE o."inDelivery" = true GROUP BY c.login;
Задание 2: SELECT track, CASE WHEN finished = true THEN 2 WHEN cancelled = true THEN -1 WHEN "inDelivery" = true THEN 1 ELSE 0 END FROM "Orders";


Автоматизация теста к API.

1. Потребуется в файле configuration изменить перемееную URL_SERVICE на корректный и действующий URL сервера;
2. Запустить тест из консоли или интерфейса PyCharm.



