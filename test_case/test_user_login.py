import allure

from common.all_api import AllApi
from tools.get_log import logs
from tools.read_yaml import ReadYaml




class TestLogin(object):

    @allure.story("登录场景")
    def test_login(self):
        e_password = AllApi().get_rsa_public_key(password="Aa123456")
        data = ReadYaml().get_data(file_path="user_login.yaml", api_name="用户密码登录")
        data["password"] = e_password
        res1 = AllApi().send_request(file_path="user_login.yaml", api_name="用户密码登录", data=data)
        logs.logger.info(res1)
        assert res1['code'] == 0 and res1['success'] == True
