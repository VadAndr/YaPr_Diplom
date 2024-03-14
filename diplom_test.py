# Вадим Андреев, 14-я когорта — Финальный проект. Инженер по тестированию плюс

import diplom_request

# Тест проверки статуса ранее созданного заказа
def test_getting_track_data():
    response = diplom_request.get_order_by_track(diplom_request.track_id)
    assert response.status_code == 200