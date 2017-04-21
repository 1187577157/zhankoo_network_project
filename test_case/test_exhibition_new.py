from modules.login import Login
from modules.zhanhui_new import New_Exhibition
from modules.all_data import all_str_data
from modules.get_data_to_excel import excel_table_by_index
import unittest
import datetime
import random
from ddt import ddt,data


@ddt
class New_Exhibition_Test(unittest.TestCase):

    the_time = datetime.datetime.now()
    the_time_less = (datetime.datetime.now() + datetime.timedelta(days=random.randint(3, 7)))
    the_time_most = (datetime.datetime.now() + datetime.timedelta(days=random.randint(7, 299)))
    current_time_less = the_time_less.strftime("%Y-%m-%d")
    current_time_most = the_time_most.strftime("%Y-%m-%d")
    current_time = the_time.strftime("%Y-%m-%d")

    def setUp(self):
        Login().send_login_request(name=18165702795,password=123456)
        all_str_data()

    def test_a_basic_info(self):
        # 调用新增基本信息
        name_in = "".join(all_str_data()[:random.randrange(1,50)])
        name = self.current_time + '测试-%s'% name_in # 展会标题
        industry = random.choice(excel_table_by_index(by_index=0)[1:])
        industry_name = industry[1]
        industry_id = int(industry[0])
        info_data = {
            'name':name,
            'industry_name':industry_name,
            'industry_id':industry_id,
            'from_on':self.current_time_less,
            'to_on':self.current_time_most
        }
        basic_info = New_Exhibition().new_basic_info(info_data)
        global exhibition_id
        exhibition_id = basic_info['ID']
        assert basic_info['success'] == True

    def test_b_zhanhui_introduction(self):
        # 调用新增展会介绍
        zhanhui_jieshao_data ="".join(all_str_data()[:random.randrange(1,1000)])
        zhanlan_fanwei_data ="".join(all_str_data()[:random.randrange(1,500)])
        zhanhui_biaoqian_data ="".join(all_str_data()[:random.randrange(1,30)]),"".join(all_str_data()[:random.randrange(1,30)])
        New_Exhibition().new_zhanhui_introduction(exhibition_id,description=zhanhui_jieshao_data,scope=zhanlan_fanwei_data ,label=zhanhui_biaoqian_data)

    def test_c_organization(self):
        # 调用新增举办机构
        zhuban_jigou_data = "".join(all_str_data()[:random.randrange(1, 120)])
        chenban_jigou_data = "".join(all_str_data()[:random.randrange(1,120)])
        New_Exhibition().new_organization(exhibition_id,organizer =zhuban_jigou_data,contractor =chenban_jigou_data)

    def test_d_boot_info(self):
        # 调用新增展位基本信息
        orderjson_data = {
            'biaozhan_price':random.randint(1, 100000),
            'biaozhan_area':random.randint(1, 100),
            'biaozhan_description':"".join(all_str_data()[:random.randrange(1,60)]),
            'guangdi_price':random.randint(1, 10000),
            'guangdi_area':random.randint(1, 100),
            'guangdi_description':"".join(all_str_data()[:random.randrange(1,60)])
        }
        New_Exhibition().new_booth_info(exhibition_id,orderjson_data)

    def test_e_exhibition_picture(self):
        # 调用上传展会图片
        picture_1 = New_Exhibition().picture_upload(index=1,filename='picture1.png')
        picture_2 = New_Exhibition().picture_upload(index=1,filename='picture2.png')
        picture_3 = New_Exhibition().picture_upload(index=1,filename='picture3.png')
        picture_4 = New_Exhibition().picture_upload(index=1,filename='picture4.png')
        picture_5 = New_Exhibition().picture_upload(index=1,filename='picture5.png')
        picture_all = [picture_1,picture_2,picture_3,picture_4,picture_5]
        images = ',' + random.choice(picture_all) + ',' + random.choice(picture_all) + ',' + random.choice(picture_all) + ',' + random.choice(picture_all) + ',' + random.choice(picture_all)
        #调用保存展会图片
        New_Exhibition().save_exhibition_picture(exhibition_id,images)

    def test_f_meeting(self):
        meeting_url = New_Exhibition().picture_upload(index=2, filename='picture6.png')
        # 调用上传同期会议图片
        meeting_title = "".join(all_str_data()[:random.randrange(10,30)])
        meeting_from_on = str(self.current_time_less)
        meeting_to_on = str(self.current_time_most)
        address = "".join(all_str_data()[:random.randrange(10,50)])
        max_people = random.randrange(2,100)
        descrition = "".join(all_str_data()[:random.randrange(10,100)])
        new_meeting_data = {
            'meeting_title':meeting_title,
            'meeting_from_on':meeting_from_on,
            'meeting_to_on':meeting_to_on,
            'address':address,
            'organizer':'深圳展酷网络有限公司',
            'max_people':max_people,
            'image-url':meeting_url,
            'descrition':descrition
        }
        New_Exhibition().new_meeting(exhibition_id,new_meeting_data)
        # 调用保存同期会议

    def test_g_contact_info(self):
        #调用新增联系人信息
        contact_info_data = {
            'contact':'测试',
            'telephone':'0755-86337066',
            'mobile':'13690769964',
            'fax':'0755-86337066',
            'qq':'1187577157',
            'email':'1187577157@qq.com'
        }
        New_Exhibition().contact_info(exhibition_id,contact_info_data)

    def test_h_exhibition_data_info(self):
        #调用新增展会数据
        textfield_type_1 = "".join(all_str_data()[:random.randrange(2, 15)])
        textfield_type_2 = "".join(all_str_data()[:random.randrange(2, 15)])
        textfield_type_3 = "".join(all_str_data()[:random.randrange(2, 15)])
        textfield_type_4 = "".join(all_str_data()[:random.randrange(2, 15)])
        exhibition_data_info = {
            'area':random.randrange(1,100000),
            'net_area':random.randrange(1,99999),
            'history_num':random.randrange(0,100),
            'viewer_quantity':random.randrange(1,50000),
            'textfield_type_1':textfield_type_1,
            'textfield_percent_1':'60',
            'exhibition_quantity':random.randrange(1,50000),
            'textfield_type_2':textfield_type_2,
            'textfield_percent_2':'40',
            'exhibition_quantity':random.randrange(1,50000),
            'textfield_type_3':textfield_type_3,
           'textfield_percent_3':'30',
           'textfield_type_4':textfield_type_4,
           'textfield_percent_4':'70' ,
           'viewer_satisfy':random.randrange(1,100),
           'exhibitor_satisfy':random.randrange(1,100)
        }
        New_Exhibition().new_exhibition_data(exhibition_id,exhibition_data_info)

    def test_i_exhibitor(self):
        #调用新增展商名录
        exhibitor_list_1 = "".join(all_str_data()[:random.randrange(8, 15)])
        exhibitor_list_2 = "".join(all_str_data()[:random.randrange(8, 15)])
        New_Exhibition().new_exhibitor(exhibition_id,exhibitor_list=exhibitor_list_1+','+exhibitor_list_2)

    def test_j_edit_back_exhibition(self):
        #调用后台编辑审核、签约展会信息
        New_Exhibition().back_edit_zhanhui(exhibition_id)

    @data(*range(12))
    def test_k_add_zhanwei(self,x):
        #调用新增展位信息
        zhanwei_num = 'BoothNo'+ str(random.randrange(1,888))
        length = random.randrange(1,25)
        width = random.randrange(1,25)
        area = length * width
        description = "".join(all_str_data()[:random.randrange(0, 20)])
        zhanwei_data = {
            'zhanwei_num':zhanwei_num,
            'zhanguang_num':'深圳会展中心馆',
            'zhanwei_xingshi':random.randrange(1,2),
            'kaikou_leixing':random.randrange(1,5),
            'price':random.randrange(1,10000),
            'area':area,
            'length':length,
            'width':width,
            'discount':random.randrange(1,10),
            'is_sell':1,
            'description':description
        }
        New_Exhibition().add_zhanwei(exhibition_id,zhanwei_data)

    def test_l_zhanwei_peizhi_xinxi(self):
        #调用新增展位配置信息
        standard_booth_config = "".join(all_str_data()[:random.randrange(1, 30)])
        New_Exhibition().zhanwei_peizhi_xinxi(exhibition_id,standard_booth_config)

    def test_m_save_zhanwei_picture(self):
        #调用上传展位图片
        zhanwei_picture = New_Exhibition().picture_upload(index=3, filename='picture6.png')
        New_Exhibition().save_zhanwei_picture(exhibition_id,zhanwei_picture)

    def test_n_back_update_zhanhui_index(self):
        #调用后台更新展会索引
        New_Exhibition().back_update_zhanhui_index()


