import base64
import json

from Crypto.Cipher import PKCS1_v1_5
from Crypto.PublicKey import RSA

from common.login import Header
from tools.read_yaml import ReadYaml
from common.http_service import RunMethod
from tools.get_log import logs


class AllApi(object):

    def __init__(self):
        self.read = ReadYaml()
        self.run = RunMethod()
        self.logger = logs
        self.header = Header()

    def send_request(self, file_path, api_name, data= None):
        try:

            method = self.read.get_method(file_path, api_name)
            url = self.read.get_url(file_path, api_name)
            headers = self.read.get_header(file_path, api_name)
            if method == 'Get':
                headers["jsid"] = self.header.a_login()
                response = self.run.run_main(method, url, headers)
            elif method == 'Post':
                if data is None:
                    data = self.read.get_data(file_path, api_name)
                headers["jsid"] = self.header.a_login()
                response = self.run.run_main(method, url, headers, json.dumps(data))
            elif method == 'Put':
                data = self.read.get_data(file_path, api_name)
                response = self.run.run_main(method, url, headers, data)

            return response
        except Exception as e:
            self.logger.into("接口访问出错啦~ %s" % e)

    def handle_pub_key(self, key):
        """
         处理公钥
        公钥格式pem，处理成以-----BEGIN PUBLIC KEY-----开头，-----END PUBLIC KEY-----结尾的格式
        :param key:pem格式的公钥，无-----BEGIN PUBLIC KEY-----开头，-----END PUBLIC KEY-----结尾
        :return:
        """
        start = '-----BEGIN PUBLIC KEY-----\n'
        end = '-----END PUBLIC KEY-----'
        result = ''
        divide = int(len(key) / 64)
        divide = divide if divide > 0 else divide + 1
        line = divide if len(key) % 64 == 0 else divide + 1
        for i in range(line):
            result += key[i * 64: (i + 1) * 64] + '\n'
        result = start + result + end
        return result

    def rsa_encrypt(self, key, text):
        """
        RSA公钥加密
        :param key: 无BEGIN PUBLIC KEY头END PUBLIC KEY尾的pem格式key
        :param text:待加密内容
        :return result：返回RAS加密后的字符串
        """
        pub_key = self.handle_pub_key(key)
        pub = RSA.importKey(pub_key)
        cipher = PKCS1_v1_5.new(pub)
        encrypt_bytes = cipher.encrypt(text.encode(encoding='utf-8'))
        result = base64.b64encode(encrypt_bytes)
        result = str(result, encoding='utf-8')
        return result

    def get_rsa_public_key(self, password):
        res = AllApi().send_request(file_path="rsa.yaml", api_name="登陆前获取RSA密钥")
        rsa_public_key = res['data']['publicKey']
        e_password = AllApi().rsa_encrypt(rsa_public_key, password)
        return e_password



if __name__ == "__main__":
    data = AllApi().get_rsa_public_key(password="Aa123456")
    print(data)
