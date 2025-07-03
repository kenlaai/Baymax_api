
from common.public import Public
from common.config import config
import yaml

class ReadYaml(object):


    def __init__(self):
        self.get_path = Public().get_object_path()


    def read_yaml(self,file_path):
        with open(self.get_path + "/yaml_data/" + file_path, 'r', encoding='utf-8') as file:
            data = yaml.safe_load(file)

        return data



    def get_url(self, file_path, api_name):
        content = self.read_yaml(file_path)
        url = config.gateway_url + content[api_name]['url']

        return url

    def get_method(self, file_path, api_name):
        content = self.read_yaml(file_path)
        method = content[api_name]['method']
        return method

    def get_header(self,file_path, api_name):
        content = self.read_yaml(file_path)
        header = content[api_name]['headers']
        return header

    def get_data(self, file_path, api_name):
        content = self.read_yaml(file_path)
        data = content[api_name]['data']

        return data

    def get_expected(self, file_path, api_name):
        content = self.read_yaml(file_path)
        expected = content[api_name]['expected']
        return expected



if __name__ == "__main__":
    data = ReadYaml().get_url('open_account.yaml', 'account')
    print(data)
