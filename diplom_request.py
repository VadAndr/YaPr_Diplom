import configuration
import requests
import data

def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,  # подставляем полный url
                         json=body)  # тут тело
response = post_new_order(data.order_body)

# Сохранение номера трека заказа, добавлена переменная, в которой запомнен трек заказа.
track_id = response.json()["track"]

# Получение заказа по треку заказа
def get_order_by_track(track_id):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_BY_TRACK + "?t=" + str(track_id))
