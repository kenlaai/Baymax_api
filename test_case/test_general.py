import allure
import pytest
from common.all_api import AllApi
from common.login import Header
# from common.public import Public
from tools.get_log import logs
from tools.read_yaml import ReadYaml


# jsid = Header().get_token()

@allure.story('工单')
@pytest.mark.usefixtures("init_token")
class TestGeneral(object):

    @pytest.fixture(scope="class")
    def init_general(self):
        logs.logger.info("\n =========================【通用】测试用例开始================================")


    @pytest.mark.parametrize('api_name',[{"提交工单"},{"提交工单-1"}])
    def test_submit_workOrder(self,api_name):
        logs.logger.info("\n ==========================用例名称：提交工单=================================")
        res = AllApi().send_request(file_path="general.yaml", api_name="提交工单")
        logs.logger.info(res)
        assert res['code'] == 0 and res['success'] == True