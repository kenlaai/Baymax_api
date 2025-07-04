import allure
import pytest

from common.all_api import AllApi
from tools.get_log import logs


@allure.story("开户")
@pytest.mark.usefixtures("init_token")
class TestOpenAccount(object):

    @pytest.fixture(scope="class")
    def init_openAccount(self):
        logs.logger.info("\n ======================【开户】测试用例开始===================================")


    def test_openAccount(self):
        res = AllApi().send_request(file_path="open_account.yaml", api_name="获取账户列表")

        logs.logger.info(res)
        assert res['code'] == 0 and res['success'] == True

