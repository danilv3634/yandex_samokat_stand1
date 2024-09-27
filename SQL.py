Первое задание 2 часть диплом
#Подсчёт заказов доставки для каждого курьера
1. SELECT c.login, COUNT(o.id) AS inDelivery #Отобразить логин курьера и количество доставок со статусом inDelivery
FROM "Couriers" AS c #Из таблицы "Курьеры"
INNER JOIN "Orders" AS o ON c.id = o."courierId" #Объединяем таблицу "Заказов" и "Курьеры"
WHERE o."inDelivery" = true #Заказы в статусе "В доставке"
GROUP BY c.login;#Группировка по логину курьера
Второе задание:
2. SELECT track, #Отобразить трек номер
    CASE
        WHEN finished = true THEN '2' # Статус 2 - завершён
        WHEN cancelled = true THEN '-1' # Статус -1 - отменён
        WHEN "inDelivery" = true THEN '1' # Статус 1 - в доставке
        ELSE '0'# Статус 0 - другой
        END AS status
   FROM "Orders";
