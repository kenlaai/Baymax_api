import requests

class RunMethod(object):

    def post_main(self,url, headers, data):
        requests.packages.urllib3.disable_warnings()

        response = requests.post(url=url, headers=headers, data=data, verify=False)
        return response

    def get_main(self,url, headers, data=None):
        requests.packages.urllib3.disable_warnings()

        response = requests.get(url=url, headers=headers, data=data, verify=False)
        return response

    def put_main(self, url, headers, data):
        requests.packages.urllib3.disable_warnings()

        response = requests.post(url=url, headers=headers, data=data, verify=False)
        return response

    def run_main(self, method, url, headers, data=None):
        requests.packages.urllib3.disable_warnings()

        requests.adapters.DEFAULT_RETRIES = 5

        if method == "Post":
            res = self.post_main(url, headers , data)

        elif method == "Get":
            res = self.get_main(url, headers)

        elif method == "Put":
            res = self.put_main(url, headers, data)

        return res.json()