import configuration
import requests
import data

def post_new_order():
    response_new_order = requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
                         json=data.order_body)
    return response_new_order


def order_info_track(track):
    response_info_track = requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_TRACK.format(track=track))
    return response_info_track
