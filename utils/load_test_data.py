'''
@Project:automationintesting
@Time:2026/6/1 15:35
@Author:Administrator
'''
import pytest
import yaml
import os

def load_room_test_data():
    file_path = r"D:\软件测试\自动化测试\automationintesting\test_data\rooms_data.yml"
    print("文件存在?", os.path.exists(file_path))
    with open(file_path, "r", encoding="utf-8") as f:
        raw = f.read()
        print("原始内容长度:", len(raw))
        print("原始内容前200字符:", raw[:200])
        f.seek(0)  # 回到文件开头
        try:
            data = yaml.safe_load(f)
            print("解析后 data 内容:", data)
        except yaml.YAMLError as e:
            print("YAML解析错误:", e)
            return None
    return data['rooms']

@pytest.mark.parametrize('room_data',load_room_test_data())
def test_add_room(room_data):
    print(room_data)


# if __name__ == "__main__":
#     data=load_room_test_data()
#     print(type(data["rooms"][0]))