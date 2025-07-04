import pytest

from common.all_api import AllApi
from tools.get_log import logs


@pytest.fixture(scope="session")
def init_token():
    logs.logger.info("\n ==========================在所有用例执行之前，生成token============================")
    AllApi().user_login(file_path="user_login.yaml", api_name="用户密码登录", password="Aa123456")



