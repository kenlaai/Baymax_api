import os
from datetime import datetime
from typing import Dict, Any

import yaml
import json

from common.public import Public
from tools.get_log import logs


# 把token值写到配置文件access_token.yml中
def write_token(res: Dict[str, Any]) -> None:

    try:
        curPath = os.path.abspath(os.path.dirname(__file__))
        yamlPath = os.path.abspath(os.path.dirname(curPath) + os.path.sep + "yaml_data/access_token.yaml")
         # print(yamlPath)

        # yaml_dir.mkdir(exist_ok=True, parents=True)
        # 3. 验证输入数据
        if not isinstance(res, dict):
            raise ValueError("Input must be a dictionary")

        # token = res.get('data', {}).get('accessToken')
        token = res['data']['accessToken']
        if not token:
            raise KeyError("Missing 'data.access_token' in response")

        # 4. 准备写入数据
        token_data = {
            'access_token': token
            }

        # 5. 原子化写入（避免写入部分数据）
        # temp_path = f"{yamlPath}.tmp"
        with open(yamlPath, 'w', encoding='utf-8') as f:
            yaml.safe_dump(token_data, f, sort_keys=False, allow_unicode=True)

        # 6. 重命名确保原子性（Unix系统保证，Windows可能需要额外处理）
        # os.replace(temp_path, yamlPath)

        logs.logger.info(f"Token successfully saved to {yamlPath}")

    except Exception as e:
        logs.logger.error(f"Failed to save token: {str(e)}")
        # 清理可能的临时文件
        # if 'temp_path' in locals() and os.path.exists(temp_path):
        #     os.unlink(temp_path)
        # raise



        # tokenValue = {
        #     'access_token': res['data']['access_token']
        # }
        # with open(yamlPath, 'w', encoding='utf-8') as f:
        #     yaml.dump(tokenValue, f)
        #
        # logs.logger.info("\n token值已保存至配置文件中")




def read_token():
    # curPath = os.path.abspath(os.path.dirname(__file__))
    # path = Public().get_object_path() + "/yaml_data/access_token.yml"
    # path = os.path.dirname(os.path.abspath('.'))+'/data/access_token.yml'
    curPath = os.path.abspath(os.path.dirname(__file__))
    path = os.path.abspath(os.path.dirname(curPath) + os.path.sep + "yaml_data/access_token.yaml")
    file = open(path)
    read = file.read()
    load = yaml.load(read, Loader=yaml.FullLoader)
    file.close()
    return load['access_token']

if __name__ == '__main__':
    res = read_token()
    print(res)