from utils.readFile import FileRead
from core.FindPath import FindPath
import os

path = os.path.join(FindPath.ReadConfig(), 'setting.ini')
# print(path)
ini_data = FileRead().read_ini(path=path)
section = 'mysql'
print(ini_data.get(section=section,option='host'))
print("test")