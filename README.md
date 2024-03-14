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
Задание 1:  SELECT c.login, COUNT(o."id") AS ordersindelivery FROM "Couriers" AS c LEFT JOIN "Orders" AS o ON c.ID
 = o."courierId" WHERE o."inDelivery" = true GROUP BY c.login;
Задание 2: SELECT track, CASE WHEN finished = true THEN 2 WHEN cancelled = true THEN -1 WHEN "inDelivery" = true THEN 1 ELSE 0 END FROM "Orders";

Скриншоты результатов запроса:

Задание 1 - сheck_created_orders_in_the_database.
Задание 2 - сheck_correctness_order_status.


Автоматизация теста к API.

1. Для корректного запуска теста потребуется установить библиотеки Pytest и request. Сделать это можно через консоль.
Выполнив команды: pip install pytest и pip install requests. Если команда pip не работает — попробуй ввести вместо этого pip3.
Также можно установить библиотеки с помощью вкладки Python Packages. Для этого:
- Необходимо открыть вкладку Python Packages на нижней панели.
- В поисковой строке наберать Pytest и requests соответственно.
- В списке выберать требуемый пакет.
- Нажать Install. 

2. Потребуется в файле configuration изменить перемееную URL_SERVICE на корректный и действующий URL сервера;

3. Запустить тест из консоли или интерфейса PyCharm.

а) Запуск тестов из терминала PyCharm.
На панели вспомогательных инструментов необходимо открыть вкладку Terminal. Рабочей директорией по умолчанию будет текущий проект. 
Запустить все тесты в проекте: pytest 
Далее запустить тесты в файле diplom_test.py: pytest diplom_test.py.

б) Запуск тестов из интерфейса PyCharm

- В поле выбора конфигурации выбрать пункт Edit Configurations.
- В открывшемся окне нажать значок «+» (Add New Configuration).
- В списке конфигураций выберать Python tests ? pytest.
- По умолчанию в строке Target выбрать Script path. Оставить выбор без изменений.
- В поле под строкой Target выберать файл с тестом - diplom_test.py.
- Нажать кнопку Apply, а затем OK.
- Запустить созданную конфигурацию с помощью зелёной стрелки.

Скриншот результата теста - test_screen.



