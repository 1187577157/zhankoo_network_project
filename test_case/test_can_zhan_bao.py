import unittest
import random
import datetime
from modules.can_zhan_bao import CanZhanBao
from modules.all_data import all_str_data

class Can_Zhan_Bao_test(unittest.TestCase):

    the_time = (datetime.datetime.now() + datetime.timedelta(days=random.randint(1,100)))
    after_time = the_time.strftime("%Y-%m-%d")

    def test_book_zhanwei(self):
        #调用预定展位
        require_area = ['9m²','18m²','27m²','36m²','45m²','54m²','72m²','90m²','108m²','9-18m²','19-36m²','37-54m²','55-72m²','73-108m²','109-200m²','200m²以上']
        enterprise = "".join(all_str_data()[:random.randrange(1, 20)])
        main_product = "".join(all_str_data()[:random.randrange(1, 10)])
        intent_exhibition = "".join(all_str_data()[:random.randrange(1, 30)])
        is_first_exhibit = [0,1]
        book_zhanwei_data = {
            'contact': '测试',
            'mobil': 13690769964,
            'from_site': 10,
            'from_site_location': 'Home_Index_RightNav',
            'enterprise': enterprise,
            'main_product': main_product,
            'is_first_exhibit': random.choice(is_first_exhibit),
            'intent_city': '广东深圳',
            'exhibiti_on': self.after_time,
            'require_area': random.choice(require_area),
            'intent_exhibition':intent_exhibition
        }
        CanZhanBao().book_zhanwei(book_zhanwei_data)

    def test_book_zhanzhuang(self):
        #调用预定展装服务
        exhibition_name = "".join(all_str_data()[:random.randrange(1,30)])
        enterprise = "".join(all_str_data()[:random.randrange(1,20)])
        budget = ['2万以下','2~3万','3~5万','5~8万','8~12万','12~18万','18~25万','25~30万','30万以上']
        service_item = ['会展设计', '会展搭建', '会展设计+搭建']
        book_zhanzhuang_data = {
            'contact':'测试',
            'mobil':13690769964,
            'from_site':'10',
            'from_site_location':'Home_Index_RightNav',
            'service_item':random.choice(service_item),
            'exhibition_name':exhibition_name,
            'tooth_area':random.randint(1,100),
            'finish_on':self.after_time,
            'budget':random.choice(budget),
            'enterprise':enterprise,
        }
        CanZhanBao().book_zhanzhuang(book_zhanzhuang_data)