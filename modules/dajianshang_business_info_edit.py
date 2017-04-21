import re
import os
import json
from modules.login import Login
from bs4 import BeautifulSoup

class Dajianshang_Business_Info_Edit:
    #编辑搭建商商家资料
    dajianshang_session = Login().send_login_request(name=18019237332,password=123456)
    back_session = Login().send_back_login_request()

    def  upload_picture(self,filename,data):
        #上传图片
        '''
        data==1为logo图片
        data==2为banner图片
        data==3为公司形象图片或案例图片
        data==4为公司资质图片
        data==5为设计师图片
        '''
        picture_save_url = 'http://exh.zhankoo-uat.com/Home/PictureSave'
        if data == 1:
            data = {
                'Width':130,
                'Height':130,
                'Prefix':'EnterpriseLogo',
                'CallBack':'parent.OnEnterpriseLogoComplete'
            }
        elif data == 2:
            data = {
                'Width': 130,
                'Height': 130,
                'Prefix': 'EnterpriseBanner',
                'CallBack': 'parent.OnEnterpriseBannerComplete'
            }
        elif data == 3:
            data = {
                'Index':'',
                'Width': 460,
                'Height': 280,
                'Prefix': 'EnterpriseStyle',
                'CallBack': 'parent.OnComplete'
            }
        elif data == 4:
            data = {
                'Width': 220,
                'Height': 150,
                'Prefix': 'Qualification',
                'CallBack': 'parent.OnQualificationComplete'
            }
        elif data == 5:
            data = {
                'Width': 120,
                'Height': 120,
                'Prefix': 'Designer',
                'CallBack': 'parent.OnDesignerComplete'
            }
        current = os.getcwd()
        base = current.split('\\test_case')[0]
        target = base + '\\data_file\\' + filename
        open_file = {'file': open(target, 'rb')}
        web_request_picture_save = self.dajianshang_session.post(url=picture_save_url,data=data,files=open_file)
        soup = BeautifulSoup(web_request_picture_save.text,'lxml')
        picture_url = re.findall(r'"pictureUrl":"(.+?)"\,"pictureSizeUrl"',str(soup))[0]
        return picture_url

    def basic_info_save(self,param):
        #编辑基本信息
        basic_info_save_url ='http://exh.zhankoo-uat.com/Decorate/Decorator/BasicSave'
        data = {
            'EnterpriseName':param['enterprise_name'],
            'EnterpriseIntroduce':param['enterprise_introduce'],
            'EnterpriseLogo':param['enterprise_logo'],
            'EnterpriseBanner':param['enterprise_banner'],
            'EnterpriseStyleImageUrl':param['enterprise_style_image_url'],
            'X-Requested-With':'XMLHttpRequest'
        }
        web_reuquest = self.dajianshang_session.post(url=basic_info_save_url,data=data)
        assert json.loads(web_reuquest.text)['success']

    def service_scope_save(self,param):
        #编辑服务范围
        service_scope_save_url = 'http://exh.zhankoo-uat.com/Decorate/Decorator/ServiceScopeSave'
        service_item_json = [{"Name": param['item_name_1'], "ID":param['item_id_1']}]
        service_area_json = [{"Name":param['area_name_1'], "Code":param['code_1'], "ParentCode":param['parent_code_1']}]
        data = {
            'CountryName':param['country_name'],
            'ProvinceName':param['province_name'],
            'CityName':param['city_name'],
            'CountyName':'',
            'ServiceItemJson':service_item_json,
            'ServiceAreaJson':service_area_json,
            'MinTakePrice':param['min_take_price'],
            'MinTakeArea':param['min_take_area'],
            'InternatType':param['internat_type'],
            'CountryCode':param['country_code'],
            'ProvinceCode':param['province_code'],
            'CityCode':param['city_code'],
            'CountyCode':'',
            'X-Requested-With':'XMLHttpRequest'
        }
        web_reuqest = self.dajianshang_session.post(url=service_scope_save_url,data=data)
        print( json.loads(web_reuqest.text))

    def qualification_save(self,param):
        #添加公司资质
        qualification_save_url = 'http://exh.zhankoo-uat.com/Decorate/Decorator/QualificationSave'
        data = {
            'ID':0,
            'Name':param['name'],
            'ImageUrl':param['image_url'],
            'Order':'',
            'X-Requested-With':'XMLHttpRequest'
        }
        web_request = self.dajianshang_session.post(url=qualification_save_url,data=data)
        assert json.loads(web_request.text)['success']

    def designer_save(self,param):
        #添加设计师
        designer_save_url = 'http://exh.zhankoo-uat.com/Decorate/Decorator/DesignerSave'
        data = {
            'ID':0,
            'Name':param['name'],
            'Title':param['title'],
            'Introduce':param['introduce'],
            'ImageUrl':param['image_url'],
            'State':param['state'],
            'Order':'',
            'X-Requested-With':'XMLHttpRequest'
        }
        web_request = self.dajianshang_session.post(url=designer_save_url,data=data)
        assert json.loads(web_request.text)['success']

    def decorate_case_save(self,param):
        #添加公司案例

        decorate_case_save_url = 'http://exh.zhankoo-uat.com/Decorate/Decorator/DecorateCaseSave'
        data = {
            'ID':0,
            'Title':param['title'],
            'Description':param['description'],
            'IndustryName':param['industry_name'],
            'IndustryID':param['industry_id'],
            'Area':param['area'],
            'BoothStandardType':param['booth_standard_type'],
            'Material':param['material'],
           'Style':param['style'],
            'DesignerID':param['designer'],
            'Price':param['price'],
            'Order':'',
            'colorAddId':param['color_add_id'],
            'Color':param['color'],
            'DecorateCaseImage':param['docorate_case_image'],
            'X-Requested-With':'XMLHttpRequest'
        }
        web_request = self.dajianshang_session.post(url=decorate_case_save_url,data=data)
        assert json.loads(web_request.text)['success']

if __name__ == '__main__':
    Dajianshang_Business_Info_Edit().decorate_case_save()