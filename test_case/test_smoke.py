'''
@Project:automationintesting
@Time:2026/6/11 0:50
@Author:Administrator
'''

import requests
import pytest
from utils.Api_Client import ApiClient
@pytest.mark.smoke
def test_smoke():

    payload = {
        'username': 'admin',
        'password': 'password'
    }
    headers = {
        'Content-Type': 'application/json'
    }
    response = ApiClient.post('/api/auth/login',json = payload,headers=headers)
    assert response.status_code == 200 ,\
        f'期望响应码200，实际响应码{response.status_code}'
    assert 'token' in response.json() and bool(response.json()['token']),\
        f'期望响应内容token有值，实际token值{response.json()["token"]}，实际响应内容{response.json()}'