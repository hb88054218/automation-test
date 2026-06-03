'''
@Project:automationintesting
@Time:2026/5/31 16:08
@Author:Administrator
'''

import requests
def test_select_rooms(api_client,temp_room):
    #url
    #url='https://automationintesting.online/api/room'
    #请求体
    #请求头
    #headers ={
    #    'cookie' : f'{get_token}'
    #}
    #发起请求
    #response = requests.get(url, headers='')
    response = api_client.get('/api/room')
    #断言状态码
    assert response.status_code == 200, \
        f"期望状态码为200，实际状态码为{response.status_code}"
    #获取返回内容
    response_data = response.json()
    rooms_list = response_data['rooms']
    #actual_room_id = None
    #断言返回内容
    assert any(i.get('roomid') == temp_room for i in rooms_list), \
        f"未找到 roomid 为 {temp_room} 的房间"

