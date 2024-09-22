'''返回相关文件地址'''
import os


class FindPath:
    __absPath = os.path.abspath(__file__)
    __corefilePath = os.path.dirname(__absPath)
    __rootPath = os.path.dirname(__corefilePath)
    def __init__(self):
        pass

    @classmethod
    def ReadProjectPath(cls):
        return cls.__rootPath

    @classmethod
    def ReadDataPath(cls):
        return os.path.join(cls.__rootPath, 'data')

    @classmethod
    def ReadLogoPath(cls):
        return os.path.join(cls.__rootPath, 'log')

    @classmethod
    def ReadConfig(cls):
        return os.path.join(cls.__rootPath, 'config')
# print(FindPath.ReadProjectPath())
# print(FindPath.ReadDataPath())