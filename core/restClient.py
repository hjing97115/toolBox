import requests,os
from utils.readFile import FileRead
from utils.FindPath import FindPath
from utils.PrintLog import logger

config = os.path.join(FindPath.ReadConfig(), "setting.ini")
class RestClient:
    def __init__(self, env):
        if(env not in ['UAT' , 'PRD']):
            raise Exception('执行环境必须为UAT或者PRD,现在的环境是{}'.format(env))
        self.api_domain = FileRead.read_ini(config).get(section=env, option='domain')

    @classmethod
    def get(cls, path, **kwargs):
        instance = cls('UAT')
        return cls.request(instance.api_domain, path=path, method="GET", **kwargs)

    @classmethod
    def post(cls, path, **kwargs):
        instance = cls('UAT')
        return cls.request(instance.api_domain, path=path, method="POST", **kwargs)

    @classmethod
    def put(cls, path, **kwargs):
        instance = cls('UAT')
        return cls.request(instance.api_domain, path=path, method="PUT", **kwargs)

    @staticmethod
    def request(api_domain, path, method, **kwargs):
        url = f"{api_domain}{path}"
        RestClient.request_log(url=url, method=method,**kwargs)
        if method == "GET":
            return requests.get(url=url, **kwargs)
        if method == "POST":
            return requests.get(url=url, **kwargs)
        if method == "PUT":
            return requests.get(url=url, **kwargs)
        # else:
        #     raise Exception('方法必须是GET、POST、PUT，输入的是{}'.format(method))

    @staticmethod
    def request_log(url, method, **kwargs):
        data = dict(**kwargs).get("data")
        json_data = dict(**kwargs).get("json")
        params = dict(**kwargs).get("params")
        headers = dict(**kwargs).get("headers")

        logger.info("接口请求的地址>>>{}".format(url))
        logger.info("接口请求的方法>>>{}".format(method))
        if data is not None:
            logger.info("接口请求的data参数>>>\n{}".format(json.dumps(data, ensure_ascii=False, indent=2)))
        if json_data is not None:
            logger.info("接口请求的json参数>>>\n{}".format(json.dumps(json_data, ensure_ascii=False, indent=2)))
        if params is not None:
            logger.info("接口请求的params参数>>>\n{}".format(json.dumps(params, ensure_ascii=False, indent=2)))
        if headers is not None:
            logger.info("接口请求的headers参数>>>\n{}".format(json.dumps(headers, ensure_ascii=False, indent=2)))

RestClient("UAT").get("/?sfrom=baidu-top").headers