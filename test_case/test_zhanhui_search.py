import unittest
from modules.zhanhui_search import zhanhui_search
from modules.get_var_fun import Get_Var_Fun

class Zhanhui_Search_Test(unittest.TestCase):

    def test_zhanhui_search(self):
        #调用展会搜索
        keyword = Get_Var_Fun().zhubanfang_zhanhui_liebiao_var()[0]
        zhanhui_search().zhanhui_search(keyword)
