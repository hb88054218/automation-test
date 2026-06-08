'''
@Project:automationintesting
@Time:2026/6/5 0:22
@Author:Administrator
'''
import requests
import pytest

from utils.load_test_data import load_reserve_test_data


@pytest.mark.parametrize('reserve_data',load_reserve_test_data())
def test_booking_room(api_client,reserve_data,booking_cleaner):
    #入参
    # payload = {
    #         "roomid": reserve_data['roomid'],
    #         "firstname": reserve_data['firstname'],
    #         "lastname": reserve_data['lastname'],
    #         "depositpaid": reserve_data['depositpaid'],
    #         "bookingdates": {
    #             "checkin": reserve_data['bookingdates']["checkin"],
    #             "checkout": reserve_data['bookingdates']['checkout']
    #         },
    #         "email": reserve_data['email'],
    #         "phone": reserve_data['phone']
    # }
    #动态入参
    bookingdates = {}
    bd = reserve_data.get('bookingdates',{})
    if 'checkin' in bd:
        bookingdates['checkin'] = bd['checkin']
    if 'checkout' in bd:
        bookingdates['checkout'] = bd['checkout']
    payload = {}
    for field in ["roomid","firstname","lastname","depositpaid","email","phone"]:
        if field in reserve_data:
            payload[field] = reserve_data[field]
        if bookingdates:
            payload['bookingdates'] = bookingdates
    #发起请求
    response = api_client.post('/api/booking',json=payload)
    #断言状态码
    assert response.status_code == reserve_data['expected_status'],\
        f"期望状态码{reserve_data['expected_status']},实际状态码{response.status_code}"
    #断言响应内容
    response_data = response.json()

    if response.status_code == 201:
        booking_id = response_data["bookingid"]
        booking_cleaner(booking_id)
        actual_checkin = response_data["bookingdates"]['checkin']
        actual_checkout = response_data["bookingdates"]['checkout']
        has_result = actual_checkin == reserve_data['bookingdates']["checkin"] and actual_checkout == reserve_data['bookingdates']["checkout"]
        assert has_result == reserve_data['expected_result']  ,\
            f'不匹配，期望响应入住日期范围：{reserve_data["bookingdates"]["checkin"]}--{reserve_data["bookingdates"]["checkout"]}，实际响应入住日期范围：{actual_checkin}--{actual_checkout}'
    else:
        has_result = "errors" in response_data and bool(response_data["errors"])
        assert has_result == reserve_data['expected_result'],\
            f'不匹配，期望响应结果：{reserve_data["expected_result"]},实际响应结果{has_result}，响应内容{response_data}'