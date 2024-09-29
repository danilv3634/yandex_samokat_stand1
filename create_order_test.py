# Виноградов Даниил, 21-я когорта — Финальный проект. Инженер по тестированию плюс

import data
from sender_stand_request import create_order, get_order_info_by_track


def test_get_order_info_by_track():
    track = create_order(data.order_body).json()['track']
    response = get_order_info_by_track(track)
    assert response.status_code == 200
