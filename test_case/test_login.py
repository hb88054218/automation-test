'''
@Project:automationintesting
@Time:2026/5/31 15:05
@Author:Administrator
'''
import requests
import pytest
@pytest.mark.parametrize('username,password,expected_status,expect_token',[
    ('admin','password',200,True),
    ('admin','wrong',401,False),
    ('','password',401,False),
    ('admin','',401,False),
    ("invalid_user", "password", 401, False)
])
def test_login(username,password,expected_status,expect_token):
    """
    合法登录场景，错误密码登录，账号为空登录，密码为空登录，不存在账号登录
    """
    # 1. 定义接口请求URL
    url= 'https://automationintesting.online/api/auth/login'
    # 2. 定义请求体（payload）为一个字典
    payload = {
        'username': username,
        'password': password
    }
    # 3. 定义请求头，通常指定内容类型为JSON
    hearders = {
        'content_type': 'application/json'
    }
    # 4. 发送POST请求，json=参数会自动将字典转为JSON字符串并设置Content-Type
    #    注意: 必须使用 json=payload 而不是 data=payload
    response  = requests.post(url, json=payload, headers=hearders)
    # 5. 断言HTTP响应状态码是否符合预期
    assert response.status_code == expected_status, \
        f"期望状态码为{expected_status}，实际状态码为{response.status_code}"
    # 6. 将响应内容解析为Python字典（假设服务器返回JSON格式）
    response_data = response.json()
    # 7. 断言token是否符合预期
    has_token = 'token' in response_data and bool(response_data['token'])
    # 8. 断言token字段的值不为空（值存在且长度大于0）
    assert has_token == expect_token , \
    f'期望token为{expect_token},实际token{has_token},返回内容{response_data}'
    # 9. 可选：打印token值，方便查看（通常用于调试）