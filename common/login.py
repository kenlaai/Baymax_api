from common.all_api import AllApi
from tools.get_log import logs
from tools.read_yaml import ReadYaml


class Header(object):

    def a_login(self):
        return "WG1ZbldnXzYwMTI4MjY1MzE1NzFfMC4wLjE6cHBhXz09Z0hYck1WbGJ3bEpiR3FDOGsrb0w0aA=="


    def brokerId(self):
        return "11000"



    def get_token(self):
        e_password = AllApi().get_rsa_public_key(password="Aa123456")
        data = ReadYaml().get_data(file_path="user_login.yaml", api_name="用户密码登录")
        data["password"] = e_password
        headers = ReadYaml().get_header(file_path="user_login.yaml", api_name="用户密码登录")
        res1 = AllApi().send_request(file_path="user_login.yaml", api_name="用户密码登录", data=data, headers=headers)
        # logs.logger.info(res1)
        # assert res1['code'] == 0 and res1['success'] == True
        token = res1['data']['accessToken']
        return token


if __name__ == '__main__':
    res = Header().get_token()
    print(res)
