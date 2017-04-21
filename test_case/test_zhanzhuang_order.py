import unittest
from modules.zhanzhuang_order import zhanzhuang_order
from modules.get_var_fun import Get_Var_Fun
from modules.back import Back
import random
from modules.all_data import all_str_data
import datetime

class Zhanzhuang_Order_Test(unittest.TestCase):

    the_time_less = (datetime.datetime.now() + datetime.timedelta(days=random.randint(7, 100)))
    current_time_less = the_time_less.strftime("%Y/%m/%d")

    def test_a_submit_zhanzhuang_demand(self):
        #调用个人中心提交展装需求
        exhibition_id = Get_Var_Fun().zhubanfang_zhanhui_liebiao_var()[1]
        order_id = Back().back_management_list(code=4)
        exhibition_name = Back().back_booth_order_detials(order_id)[0]
        booth_id = Back().back_booth_order_detials(order_id)[1]
        booth_name = Back().back_booth_order_detials(order_id)[2]
        the_exhibition_title = "".join(all_str_data()[:random.randrange(1,25)])
        designer_demand = "".join(all_str_data()[:random.randrange(1,200)])
        the_exhibition_demand = "".join(all_str_data()[:random.randrange(1,300)])
        service_item = ['会展设计','会展设计+搭建','会展搭建','展具搭建','交通运输','印刷包装','酒店旅游','公关策划','广告影视','礼品模特']
        submit_zhanzhuang_demand_data = {
            'the_exhibition_title':the_exhibition_title,
            'service_item':random.choice(service_item),
            'finish_on':self.current_time_less,
            'designer_demand':designer_demand,
            'the_exhibition_demand':the_exhibition_demand
        }
        zhanzhuang_order().submit_zhanzhuang_demand(exhibition_id,exhibition_name,booth_id,booth_name,submit_zhanzhuang_demand_data)

    def test_b_back_zhanzhuang_demand_confirm(self):
        #调用后台展装需求确认
        global zhanzhuang_demand_id
        zhanzhuang_demand_id = zhanzhuang_order().get_zhanzhuang_demand_list_id()
        budget = ['2万以下', '2~3万', '3~5万', '5~8万', '8~12万', '12~18万', '18~25万', '25~30万', '30万以上']
        zhanzhuang_order().back_zhanzhuang_demand_confirm(zhanzhuang_demand_id,budget=random.choice(budget))

    def test_c_back_matching_company(self):
        #调用后台匹配展装公司
        zhanzhuang_order().back_matching_company(zhanzhuang_demand_id)

    def test_d_back_demand_contract_and_price(self):
        #调用后台展装需求签订合同及定价
        price = random.randrange(1,100000)
        zhanzhuang_order().back_demand_contract_and_price(zhanzhuang_demand_id,price)

    def test_e_back_finance_zhanzhuang_demand_price(self):
        # 调用后台财务提交展装需求定价
        zhanzhuang_order().back_finance_zhanzhuang_demand_price(zhanzhuang_demand_id)

    def test_f_zhanzhuang_demand_place_order(self):
        #调用展装需求下订单
        zhanzhuang_order().zhanzhuang_demand_place_order(zhanzhuang_demand_id)