import allure
import pytest
from common.all_api import AllApi
from tools.get_log import logs


@allure.story('工单')
class TestGeneral(object):

    def test_general(self):
        res = AllApi().send_request(file_path="general.yaml", api_name="提交工单")

        logs.logger.info(res)
        assert res['code'] == 0 and res['success'] == True