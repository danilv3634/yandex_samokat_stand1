#Павел Феоктистов 8-я когорта — Финальный проект. Инженер по тестированию плюс
import data
import sender_stand_request
import configuration
#Выполнить запрос на создание заказа
def create_order():
    response_create_order = sender_stand_request.post_new_order()
#Возвращаем ответ от сервера
    return response_create_order
#Проверяем, что статус код == 201
    assert create_order.status_code == 201
#Функция на сохранение трека
def get_track(order_body):
    response_create_order = create_order(order_body)
    track_order = response_create_order.json()["track"]
#Получение информации по треку
def get_info_order(track_order):
    response_info_order = sender_stand_request.order_info_track(track_order)
    return response_info_order
#Проверка, что статус 200
    assert get_info_order.status_code == 200

def test_create_get_order():
    response_create_order = create_order() #Создаём заказ
    assert response_create_order.status_code == 201 #Проверям, что заказ успешно создан
    track = response_create_order.json()["track"] #Сохраняем трек номер созданного заказа
    response_info_order = get_info_order(track) #Получаем информацию по трек номеру созданного заказа
    assert response_info_order.status_code == 200 #Проверяем успешное получение информации по трек номеру созданного заказа