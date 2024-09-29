from core.restClient import RestClient
from utils.readFile import FileRead
from utils.FindPath import FindPath
import os

config = os.path.join(FindPath.ReadConfig(), "setting.ini")
class Api(RestClient):
    def __init__(self,env):
        if (env not in ['UAT', 'PRD']):
            raise Exception('执行环境必须为UAT或者PRD,现在的环境是{}'.format(env))
        self.api_domain = FileRead.read_ini(config).get(section=env, option='domain')
        super().__init__(self.api_domain)

    def get_XXX(self, **kwargs):
        return self.get("/?sfrom=baidu-top")

    def post_yyy(self, **kwargs):
        return  self.post(("/path"))
# a = Api('UAT')
# a.get_XXX()