from modules.zhanhui_order import zhanhui_orderfrom modules.get_var_fun import Get_Var_Funimport unittestclass Zhanhui_Order_Test(unittest.TestCase):    def test_a_online_booth_order(self):        #调用展会下订单        global order_id        exhibition_id = Get_Var_Fun().zhubanfang_zhanhui_liebiao_var()[1]        booth_id = zhanhui_order().online_booth_order(exhibition_id)        order_id = zhanhui_order().booth_book_sure_order_save(exhibition_id, booth_id)    def test_b_organizer_comfirm_order(self):        #调用主办方审核展位        zhanhui_order().organizer_comfirm_order(order_id)