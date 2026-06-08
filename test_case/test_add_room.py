'''
@Project:automationintesting
@Time:2026/5/31 19:01
@Author:Administrator
'''
import requests
import pytest

from utils.load_test_data import load_room_test_data


@pytest.mark.parametrize('room_data',load_room_test_data())
def test_add_room(api_client,room_data):
    #url
    #url = 'https://automationintesting.online/api/room'
    #请求体
    # payload = {
    #     'roomName': roomName,
    #     'Type': type,
    #     'accessible': accessible,
    #     'roomPrice': roomPrice,
    #     'feature': [feature[0]]
    # }
    payload = {
        'roomName': room_data['roomName'],
        'type':  room_data['type'],
        'accessible':  room_data['accessible'],
        "description":  room_data['description'],
        "image":  room_data['image'],
        'roomPrice':  room_data['roomPrice'],
        'features': [ room_data['features'][0],
                      room_data['features'][1],
                      room_data['features'][2],
                      room_data['features'][3]]
    }
    #请求头
    # headers = {
    #     'Content-Type': 'application/json',
    #     'Cookie' : f'token={get_token}'
    # }
    #发起请求
    #response = requests.post(url,json=payload,headers=headers)
    response = api_client.post('/api/room',json=payload)
    print(response.text)
    #断言响应状态码
    assert response.status_code == room_data['expected_status'],\
        f'期望状态码{room_data['expected_status']},实际状态码{response.status_code}'
    #获取并断言响应内容
    response_data = response.json()
    has_result = 'success' in response_data and bool(response_data['success'])
    assert has_result == room_data['expected_result'],\
        f'期望响应结果{room_data['expected_result']},实际响应结果{has_result}，响应文本{response_data}'

