from modules.dajianshang_business_info_edit import Dajianshang_Business_Info_Edit
from modules.get_data_to_excel import excel_table_by_index
from modules.all_data import all_str_data
from modules.get_var_fun import Get_Var_Fun
import unittest
import random
import time

class Dajianshang_Business_Info_Edit_Test(unittest.TestCase):

    now = time.strftime('%Y_%m_%d_%H_%M_%S')

    def test_a_basic_info_save(self):
        #调用编辑基本信息
        enterprise_logo = Dajianshang_Business_Info_Edit().upload_picture(filename='picture1.png',data=1)
        enterprise_banner = Dajianshang_Business_Info_Edit().upload_picture(filename='picture2.png', data=2)
        enterprise_style_image_url1 = Dajianshang_Business_Info_Edit().upload_picture(filename='picture3.png', data=3)
        enterprise_style_image_url2 = Dajianshang_Business_Info_Edit().upload_picture(filename='picture4.png', data=3)
        enterprise_style_image_url3 = Dajianshang_Business_Info_Edit().upload_picture(filename='picture5.png', data=3)
        enterprise_style_image_url = ','+enterprise_style_image_url1+','+enterprise_style_image_url2+','+enterprise_style_image_url3
        basic_info_data = {
            'enterprise_name':'深圳展览策划有限公司',
            'enterprise_introduce':'深圳展览策划有限公司创建于2005年3月，在过去10年，亚美与中国展装行业高速发展带来的历史机遇相逢，用商业的意识、艺术的思想、科技的手段为客户提供创意、设计、制作实施的一体化服务，成为展装系统集成服务商领先地位的企业。我们为会展主场运营、展示设计与制作、美陈设计与实施、商业空间设计与施工、数字化展示与应用等提供有竞争力解决方案和服务，帮助客户在展示空间领域获得成功。公司累积10年的行业经验，拥有大型的展示制作工厂及一批专业化的服务人才。服务于众多知名企业，如FOXCONN、MITSUBISHI、SIEMENS、世茂集团、和记黄埔、东风、中粮、中国邮政集团等。在会展主场方面服务过：武汉光博会（其中2014年设计并制作47家特装企业，其中包括8000平方的富士康专馆的整体设计与搭建工作）、湖北省经委楚天杯工业设计展（8000平方，其中主展台1008平方）、湖北省旅游局旅游博览会10200平方整体承办与主场设计搭建工作等。我们坚持聚焦战略，对低碳环保循环会展系统、数字化展示与应用、云展装等持续进行研发投入，以客户需求和前沿技术创新为驱动，使公司始终处于行业前沿。 未来，亚美展示将充分融合“商业+艺术+科技”的一体化服务商业模式的优势，坚持以客户为中心，以奋斗者为本，与合作伙伴一起，开放合作，努力构建一个更加高效整合的公共平台，引领行业快速发展。45645深圳展览策划有限公司创建于2005年3月，在过去10年，亚美与中国展装行业高速发展带来的历史机遇相逢，用商业的意识、艺术的思想、科技的手段为客户提供创意、设计、制作实施的一体化服务，成为展装系统集成服务商领先地位的企业。我们为会展主场运营、展示设计与制作、美陈设计与实施、商业空间设计与施工、数字化展示与应用等提供有竞争力解决方案和服务，帮助客户在展示空间领域获得成功。公司累积10年的行业经验，拥有大型的展示制作工厂及一批专业化的服务人才。服务于众多知名企业，如FOXCONN、MITSUBISHI、SIEMENS、世茂集团、和记黄埔、东风、中粮、中国邮政集团等。在会展主场方面服务过：武汉光博会（其中2014年设计并制作47家特装企业，其中包括8000平方的富士康专馆的整体设计与搭建工作）、湖北省经委楚天杯工业设计展（8000平方，其中主展台1008平方）、湖北省旅游局旅游博览会10200平方整体承办与主场设计搭建工作等。我们坚持聚焦战略，对低碳环保循环会展系统、数字化展示与应用、云展装等持续进行研发投入，以客户需求和前沿技术创新为驱动，使公司始终处于行业前沿。 未来，亚美展示将充分融合“商业+艺术+科技”的一体化服务商业模式的优势，坚持以客户为中心，以奋斗者为本，与合作伙伴一起，开放合作，努力构建一个更加高效整合的公共平台，引领行业快速发展。45645深圳展览策划有限公司创建于2005年3月，在过去10年，亚美与中国展装行业高速发展带来的历史机遇相逢，用商业的意识、艺术的思想、科技的手段为客户提供创意、设计、制作实施的一体化服务，成为展装系统集成服务商领先地位的企业。我们为会展主场运营、展示设计与制作、美陈设计与实施、商业空间设计与施工、数字化展示与应用等提供有竞争力解决方案和服务，帮助客户在展示空间领域获得成功。公司累积10年的行业经验，拥有大型的展示制作工厂及一批专业化的服务人才。服务于众多知名企业，如FOXCONN、MITSUBISHI、SIEMENS、世茂集团、和记黄埔、东风、中粮、中国邮政集团等。在会展主场方面服务过：武汉光博会（其中2014年设计并制作47家特装企业，其中包括8000平方的富士康专馆的整体设计与搭建工作）、湖北省经委楚天杯工业设计展（8000平方，其中主展台1008平方）、湖北省旅游局旅游博览会10200平方整体承办与主场设计搭建工作等。我们坚持聚焦战略，对低碳环保循环会展系统、数字化展示与应用、云展装等持续进行研发投入，以客户需求和前沿技术创新为驱动，使公司始终处于行业前沿。 未来，亚美展示将充分融合“商业+艺术+科技”的一体化服务商业模式的优势，坚持以客户为中心，以奋斗者为本，与合作伙伴一起，开放合作，努力构建一个更加高效整合的公共平台，引领行业快速发展。45645深圳展览策划有限公司创建于2005年3月，在过去10年，亚美与中国展装行业高速发展带来的历史机遇相逢，用商业的意识、艺术的思想、科技的手段为客户提供创意、设计、制作实施的一体化服务，成为展装系统集成服务商领先地位的企业。我们为会展主场运营、展示设计与制作、美陈设计与实施、商业空间设计与施工、数字化展示与应用等提供有竞争力解决方案和服务，帮助客户在展示空间领域获得成功。公司累积10年的行业经验，拥有大型的展示制作工厂及一批专业化的服务人才。服务于众多知名企业，如FOXCONN、MITSUBISHI、SIEMENS、世茂集团、和记黄埔、东风',
            'enterprise_logo':enterprise_logo,
            'enterprise_banner':enterprise_banner,
            'enterprise_style_image_url':enterprise_style_image_url
        }
        Dajianshang_Business_Info_Edit().basic_info_save(basic_info_data)

    def test_b_service_scope_save(self):
        #调用编辑服务范围
        random_choice_item = random.choice(excel_table_by_index(by_index=1)[1:])
        item_name_1 = random_choice_item[1]
        item_id_1 = random_choice_item[0]
        random_choice_area = random.choice(excel_table_by_index(by_index=2)[1:])
        area_name_1 = random_choice_area[5]
        code_1 = random_choice_area[4]
        parent_code_1 = random_choice_area[0]
        country_name = random_choice_area[1]
        province_name = random_choice_area[3]
        city_name = random_choice_area[5]
        province_code = random_choice_area[2]
        city_code = random_choice_area[4]
        service_scope_data = {
            'item_name_1':item_name_1,
            'item_id_1':item_id_1,
            'area_name_1':area_name_1,
            'code_1':code_1,
            'parent_code_1':parent_code_1,
            'country_name':country_name,
            'province_name':province_name,
            'city_name':city_name,
            'internat_type':parent_code_1,
            'country_code':parent_code_1,
            'province_code':province_code,
            'city_code':city_code,
            'min_take_price':random.randrange(1,10),
            'min_take_area':random.randrange(10,100)
        }
        Dajianshang_Business_Info_Edit().service_scope_save(service_scope_data)

    def test_c_qualification_save(self):
        #调用添加公司资质
        name = "".join(all_str_data()[:random.randrange(1,30)])
        image_url = Dajianshang_Business_Info_Edit().upload_picture(filename='picture1.png', data=4)
        qualification_data = {
            'name':name,
            'image_url':image_url
        }
        Dajianshang_Business_Info_Edit().qualification_save(qualification_data)

    def test_d_designer_save(self):
        #调用添加设计师
        name = "".join(all_str_data()[:random.randrange(2,4)])
        title = ['设计总监','高级设计师','普通设计师']
        introduce = "".join(all_str_data()[:random.randrange(1,90)])
        image_url = Dajianshang_Business_Info_Edit().upload_picture(filename='picture3.png', data=5)
        designer_data = {
            'name':name,
            'title':random.choice(title),
            'introduce':introduce,
            'image_url':image_url,
            'state':1
        }
        Dajianshang_Business_Info_Edit().designer_save(designer_data)

    def test_e_decorate_case_save(self):
        #调用添加公司案例
        title = self.now + "".join(all_str_data()[:random.randrange(1,10)])
        description = "".join(all_str_data()[:random.randrange(1,140)])
        material = ['木质材质','桁架型材','环保材质']
        style = ['简约','现代','中式','欧式','美式','田园','新古典','混搭']
        designer = Get_Var_Fun().back_dajianshang_guangli_var()
        docorate_case_image_1 = Dajianshang_Business_Info_Edit().upload_picture(filename='picture1.png', data=3)
        docorate_case_image_2 = Dajianshang_Business_Info_Edit().upload_picture(filename='picture2.png', data=3)
        docorate_case_image_3 = Dajianshang_Business_Info_Edit().upload_picture(filename='picture3.png', data=3)
        docorate_case_image_4 = Dajianshang_Business_Info_Edit().upload_picture(filename='picture4.png', data=3)
        docorate_case_image_5 = Dajianshang_Business_Info_Edit().upload_picture(filename='picture5.png', data=3)
        docorate_case_image_all = [docorate_case_image_1,docorate_case_image_2,docorate_case_image_3,docorate_case_image_4,docorate_case_image_5]
        docorate_case_image = ','+random.choice(docorate_case_image_all)+','+random.choice(docorate_case_image_all)+','+random.choice(docorate_case_image_all)+','+random.choice(docorate_case_image_all)+','+random.choice(docorate_case_image_all)
        color = ['白色','米色','黄色','橙色','红色','粉色','绿色','蓝色','紫色','黑色','咖啡色','灰色','彩色']
        color_add_id = random.choice(color)
        decorate_case_data = {
            'title':title,
            'description':description,
            'industry_name':'办公用品',
            'industry_id':444,
            'area':random.randrange(1,100),
            'booth_standard_type':random.randrange(1,5),
            'material':random.choice(material),
            'style':random.choice(style),
            'designer':random.choice(designer),
            'price':str(random.randrange(1,100000)),
            'color_add_id':color_add_id,
            'color':color_add_id,
            'docorate_case_image':docorate_case_image
        }
        print(random.choice(color))
        Dajianshang_Business_Info_Edit().decorate_case_save(decorate_case_data)



