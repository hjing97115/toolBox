import requests,os

class RestClient:
    def __init__(self, env):
        if(env != 'UAT' and env != 'PRD'):
            raise Exception('执行环境必须为UAT或者PRD,现在的环境是{}'.format(env))
        self.api_domain = "a"

    @staticmethod
    def request(path, method, **kwargs):
        if method == "GET":
            a = RestClient.api_domain()
            return a

    @classmethod
    def get(cls, path, **kwargs):
        cls.request(path=path, method="GET", **kwargs)

print(RestClient("UAT").get("/post"))