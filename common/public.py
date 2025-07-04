import csv
import json
from pathlib import Path


class Public(object):
    def get_object_path(self):
        #
        current_file_path = Path(__file__).resolve()
        #
        project_root = current_file_path.parent.parent
        return str(project_root)

    def get_test_data_from_csv(self,csv_file):
        """从CSV文件读取测试数据"""
        with open(Public().get_object_path() + "/csv/" + csv_file, newline='', encoding='utf-8') as f:
            reader = list(csv.DictReader(f))
            token = reader[0]["token"]
            return token







if __name__ == "__main__":
    res = Public().get_test_data_from_csv(csv_file="loginData.csv")
    print(res)
