'''
@Project:automationintesting
@Time:2026/5/31 22:34
@Author:Administrator
'''
from urllib import response

import requests
import pytest
@pytest.mark.parametrize('expected_status,expected_result',[
    (202,True)
])
def test_delete_room(get_token,croom_for_room_id,expected_status,expected_result):
    #新增并获取roomid并拼接到url
    # url = 'https://automationintesting.online/api/room'
    # roomname = '1004'
    # payload = {
    #     'roomName':roomname,
    #     'type': 'Double',
    #     'accessible': True,
    #     "description": 'welcome to my hotell',
    #     "image": 'https://www.mwtestconsultancy.co.uk/img/room4.jpg',
    #     'roomPrice': '120',
    #     'features': ["WiFi",
    #                  "TV",
    #                  "Radio",
    #                  "Safe"]
    # }
    # # 请求头
    # headers = {
    #     'Content-Type': 'application/json',
    #     'Cookie': f'token={get_token}'
    # }
    # # 发起请求
    # response = requests.post(url, json=payload, headers=headers)
    # assert response.status_code == 200,\
    #     f'房间创建成功'
    # #查询刚刚创建的房间的roomid
    # url='https://automationintesting.online/api/room'
    # headers = {
    #     'Cookie': f'token={get_token}'
    # }
    # response = requests.get(url,headers=headers)
    # response_data = response.json()
    # rooms_list = response_data['rooms']
    # room_id = ()
    # for i in rooms_list:
    #     if i.get('roomName') == roomname:
    #         room_id = i.get('roomid')
    #         break
    #url
    url=f'https://automationintesting.online/api/room/{croom_for_room_id}'
    #请求体
    #请求头
    headers = {
        'Cookie': f'token={get_token}'
    }
    #发起请求
    response = requests.delete(url,headers=headers)
    #断言状态码
    assert response.status_code == expected_status,\
        f"期望状态码为{expected_status}，实际状态码为{response.status_code}"
    # #断言响应类容
    # response_data = response.json()
    # has_result = 'success' in response_data and bool(response_data['success'])
    # assert has_result == expected_result,\
    #     f'期望响应结果{expected_result},实际响应结果{has_result}，响应文本{response_data}'