'''
@Project:automationintesting
@Time:2026/5/31 18:15
@Author:Administrator
'''
import time

import requests
import pytest
import os
from utils.Api_Client import ApiClient
username = os.getenv('API_USERNAME','admin')
password = os.getenv('API_PASSWORD','password')
login_url = os.getenv('API_LOGIN_URL','https://automationintesting.online/api/auth/login')
@pytest.fixture(scope="session")
def get_token():#获取token
    payload = {
        "username": username,
        "password": password
    }
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(login_url,json=payload,headers=headers)
    assert response.status_code == 200
    if response.status_code == 200:
        response_data = response.json()
        token = response_data['token']
    if response.status_code != 200:
        raise Exception(f'登录失败')
    if token is None:
        raise Exception("登录成功但未返回 token")
    return token

@pytest.fixture(scope="session")
def api_client(get_token):#请求通信公用实例，测试函数直接调用即可
    return ApiClient(token=get_token)  #实例化过程

@pytest.fixture(scope="function")
def croom_for_room_id(get_token):#生成新的roomid
    #接口地址
    url = 'https://automationintesting.online/api/room'
    #请求体
    room_name = f'r_{int(time.time())}'
    payload = {
        'roomName': room_name,
        'type': 'Single',
        'accessible': True,
        "description": 'the room is warm and soft by auto',
        "image": 'https://www.mwtestconsultancy.co.uk/img/room.jpg',
        'roomPrice': '200',
        'features': ['WiFi']
    }
    # 请求头
    headers = {
        'Content-Type': 'application/json',
        'Cookie': f'token={get_token}'
    }
    # 发起请求POST
    response = requests.post(url, json=payload, headers=headers)
    print(response.text)
    # 断言响应状态码
    assert response.status_code == 200, \
        f'期望状态码200,实际状态码{response.status_code}'
    #获取room_id
    headers = {
        'Cookie': f'token={get_token}'
    }
    response = requests.get(url, headers=headers)
    response_data = response.json()
    rooms_list = response_data['rooms']
    room_id = ()
    for i in rooms_list:
        if i.get('roomName') == room_name:
            room_id = i.get('roomid')
            break
    if room_id is None:
        return  print(f'没有查到room_id,响应内容：{response_data}')
    return room_id

@pytest.fixture(scope="function")
def temp_room(get_token):#生成新的roomid并清理数据
    #接口地址
    url = 'https://automationintesting.online/api/room'
    #请求体
    room_name = f'r_{int(time.time())}'
    payload = {
        'roomName': room_name,
        'type': 'Single',
        'accessible': True,
        "description": 'the room is warm and soft by auto',
        "image": 'https://www.mwtestconsultancy.co.uk/img/room.jpg',
        'roomPrice': '200',
        'features': ['WiFi']
    }
    # 请求头
    headers = {
        'Content-Type': 'application/json',
        'Cookie': f'token={get_token}'
    }
    # 发起请求POST
    response = requests.post(url, json=payload, headers=headers)
    print(response.text)
    # 断言响应状态码
    assert response.status_code == 200, \
        f'期望状态码200,实际状态码{response.status_code}'
    #获取room_id
    headers = {
        'Cookie': f'token={get_token}'
    }
    response = requests.get(url, headers=headers)
    response_data = response.json()
    rooms_list = response_data['rooms']
    room_id = None
    for i in rooms_list:
        if i.get('roomName') == room_name:
            room_id = i.get('roomid')
            break
    if room_id is None:
        raise   print(f'没有查到room_id,响应内容：{response_data}')
    yield room_id
    del_room(get_token,room_id)


def del_room(get_token,room_id):#删除接口
    url = f'https://automationintesting.online/api/room/{room_id}'
    # 请求体
    # 请求头
    headers = {
        'Cookie': f'token={get_token}'
    }
    # 发起请求
    response = requests.delete(url, headers=headers)
    # 断言状态码
    assert response.status_code == 202, \
        f"期望状态码为200，实际状态码为{response.status_code}"