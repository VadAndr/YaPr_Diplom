# YaPr_Diplom

�������� ������� ������������� ����� (������ �����).

������ � ����� ������.

���������� �� ������ � SQL ���������:

1. �����: ����� ���������� � �� ��������� ��������� ���� �������: ������� ������, ��������. � ����� ������� ������ � ������.

2. ������������ � ������� �� SSH:
$ ssh 79e172fe-7b2d-441b-9085-bd2266701863@serverhub.praktikum-services.ru -p 4554

3. ������������ � ��. ������ - smith:
psql -U morty -d scooter_rent

4. ���������� � ��:
������� 1: SELECT c.login, COUNT(o."firstName") AS ordersindelivery FROM "Couriers" AS c LEFT JOIN "Orders" AS o ON c.ID = o."courierId" WHERE o."inDelivery" = true GROUP BY c.login;
������� 2: SELECT track, CASE WHEN finished = true THEN 2 WHEN cancelled = true THEN -1 WHEN "inDelivery" = true THEN 1 ELSE 0 END FROM "Orders";


������������� ����� � API.

1. ����������� � ����� configuration �������� ���������� URL_SERVICE �� ���������� � ����������� URL �������;
2. ��������� ���� �� ������� ��� ���������� PyCharm.



