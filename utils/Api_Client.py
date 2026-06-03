'''
@Project:automationintesting
@Time:2026/6/2 22:00
@Author:Administrator
'''
import requests

class ApiClient:
    """
    封装 HTTP 请求方法，自动携带认证 token。
    """
    def __init__(self, token: str = None, base_url: str = "https://automationintesting.online"):
        self.base_url = base_url.rstrip('/')
        self.session = requests.Session()
        if token:
            # 根据实际认证方式选择 Cookie 或 Authorization
            # 这里以 Cookie 为例（因为之前你用的是 Cookie: token=xxx）
            self.session.headers.update({
                'Content-Type': 'application/json',
                "Cookie": f"token={token}"
            })
            # 如果使用 Bearer Token，则改为：
            # self.session.headers.update({"Authorization": f"Bearer {token}"})

    def request(self, method: str, endpoint: str, **kwargs):
        """发送请求的通用方法"""
        url = f"{self.base_url}{endpoint}"
        # 可以在此添加日志
        print(f"发送 {method} 请求: {url}")
        response = self.session.request(method, url, **kwargs)
        # 可以在此添加响应日志
        print(f"响应状态码: {response.status_code}")
        return response

    def get(self, endpoint: str, **kwargs):
        return self.request("GET", endpoint, **kwargs)

    def post(self, endpoint: str, **kwargs):
        return self.request("POST", endpoint, **kwargs)

    def put(self, endpoint: str, **kwargs):
        return self.request("PUT", endpoint, **kwargs)

    def delete(self, endpoint: str, **kwargs):
        return self.request("DELETE", endpoint, **kwargs)