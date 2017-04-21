from modules.zhanhui_get_ticket import get_ticket
from modules.get_var_fun import Get_Var_Fun
import unittest

class Zhanhui_Ticket_Test(unittest.TestCase):

    def test_a_zhanhui_ticket(self):
        # 调用获取展会门票
        exhibition_id = Get_Var_Fun().zhubanfang_zhanhui_liebiao_var()[1]
        get_ticket().get_ticket(exhibition_id)

    def test_b_update_ticket_pass(self):
        # 调用主办方审核通过展会门票
        get_ticket().update_ticket_pass()