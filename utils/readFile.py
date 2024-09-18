'''读取各类文件'''
import configparser
import yaml
class FileRead:
    def __init__(self):
        pass

    @staticmethod
    def read_ini(path): # .get(section=, option=)
        config = configparser.ConfigParser()
        config.read(path, encoding='utf-8')
        return config

    @staticmethod
    def read_yaml(path):
        f = open(path, encoding='utf-8')
        read = yaml.safe_load_all(f)
        return read