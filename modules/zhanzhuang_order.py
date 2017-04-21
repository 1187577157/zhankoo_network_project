from modules.login import Login
import json
from bs4 import BeautifulSoup
import re

class zhanzhuang_order:

    submit_zhanzhuang_demand_url = 'http://exh.zhankoo-uat.com/Decorate/Exhibitor/DecorateBookSave'
    zhanzhuang_demand_list_url = 'http://exh.zhankoo-uat.com/Decorate/Partial/_DecorateBookFindPage'
    zhanzhuang_demand_confirm_url = 'http://back.zhankoo-uat.com/Exhibition/Decorate/DecorateBookConfirmation'
    matching_company_url = 'http://back.zhankoo-uat.com/Exhibition/Decorate/MatchingCompany'
    demand_contract_and_price_url = 'http://back.zhankoo-uat.com/Exhibition/Decorate/DecoratePriceInsert'
    financ_zhanzhuang_demand_price_url = 'http://back.zhankoo-uat.com/Exhibition/Decorate/ConfirmPrice'
    zhanzhuang_demand_place_order_url = 'http://exh.zhankoo-uat.com/Decorate/Exhibitor/SureOrderSave'
    canzhanshang_session = Login().send_login_request(name=13690769964,password=123456)
    back_session = Login().send_back_login_request()

    def submit_zhanzhuang_demand(self,exhibition_id,exhibition_name,booth_id,booth_name,param):
        #个人中心提交展装需求
        data = {
            'FromSite':10,
            'FromSiteLocation':'http://exh.zhankoo-uat.com/_Decorate_Exhibitor_DecorateBookCreate_Index',
            'Subject':param['the_exhibition_title'],
            'ExhibitorEnterpriseID':519,
            'ExhibitorEnterpriseName':'深圳展酷网络有限公司',
            'ContactIDs':134851,
            'ProvinceName':'广东省',
            'CityName':'深圳市',
            'ExhibitionID':exhibition_id,
            'ExhibitionName':exhibition_name,
            'BoothID':booth_id,
            'BoothName':booth_name,
            'ServiceItem':param['service_item'],
            'ProvinceCode':440000,
            'CityCode':440300,
            'FinishOn':param['finish_on'],
            'DesignerDemand':param['designer_demand'],
            'DecorateDemand':param['the_exhibition_demand'],
            'X-Requested-With':'XMLHttpRequest'
        }
        web_request = self.canzhanshang_session.post(url=self.submit_zhanzhuang_demand_url,data=data)
        assert json.loads(web_request.text)['success']

    def get_zhanzhuang_demand_list_id(self):
        #个人中心展装需求列表获取最新需求id
        web_request = self.canzhanshang_session.get(url=self.zhanzhuang_demand_list_url)
        soup = BeautifulSoup(web_request.text,'lxml')
        zhanzhuang_demand_id = soup.select('a')[0].get_text()
        return zhanzhuang_demand_id

    def back_zhanzhuang_demand_confirm(self,zhanzhuang_demand_id,budget):
        #后台展装需求确认
        web_request_get_param = self.back_session.get(url='http://back.zhankoo-uat.com/Exhibition/Decorate/DecorateBookDetailView/%s'% zhanzhuang_demand_id)
        soup = BeautifulSoup(web_request_get_param.text,'lxml')
        sbuject = soup.select('input')[1]['value']
        exhibitor_enterprise_name = soup.select('input')[2]['value']
        exhibition_name = soup.select('input')[4]['value']
        exhibition_from_on = soup.select('input')[5]['value']
        exhibition_to_on = soup.select('input')[6]['value']
        exhibition_address = soup.select('input')[7]['value']
        exhibition_industry = soup.select('input')[8]['value']
        exhibition_area = soup.select('input')[9]['value']
        booth_area = soup.select('input')[10]['value']
        booth_width = soup.select('input')[11]['value']
        booth_length = soup.select('input')[12]['value']
        booth_name = soup.select('input')[13]['value']
        booth_pavilion_no = soup.select('input')[14]['value']
        service_item_str = str(soup.select('input')[15]['data-options'])
        service_item = re.findall(r'\'(.+?)\'',service_item_str)[-2]
        province_name = soup.select('input')[16]['value']
        city_name = soup.select('input')[17]['value']
        designer_demand = soup.select('input')[18]['value']
        finish_on = soup.select('input')[19]['value']
        decorate_demand_str = str(soup.select('td')[66])
        decorate_demand = re.findall(r'\"(.+?)\"', decorate_demand_str)[-1]
        booth_description_str = str(soup.select('td')[60])
        booth_description = re.findall(r'\=(.+?)\<', booth_description_str)[-1][-2:]
        data ={
        'ID':zhanzhuang_demand_id,
        'Subject':sbuject,
        'ExhibitorEnterpriseName':exhibitor_enterprise_name,
        'Budget':budget,
        'ExhibitionName':exhibition_name,
        'ExhibitionFromOn':exhibition_from_on,
        'ExhibitionToOn':exhibition_to_on,
        'ExhibitionAddress':exhibition_address,
        'ExhibitionIndustry':exhibition_industry,
        'ExhibitionArea':exhibition_area,
        'BoothArea':booth_area,
        'BoothWidth':booth_width,
        'BoothLength':booth_length,
        'BoothType':'Standard',
        'BoothName':booth_name,
        'BoothPavilionNO':booth_pavilion_no,
        'BoothStandardType':'SingleDoor',
        'BoothDescription':booth_description,
        'ServiceItem':service_item,
        'ProvinceCode':440000,
        'CityCode':440300,
        'ProvinceName':province_name,
        'CityName':city_name,
        'DesignerDemand':designer_demand,
        'FinishOn':finish_on,
        'DecorateDemand':decorate_demand
        }
        web_request = self.back_session.post(url=self.zhanzhuang_demand_confirm_url,data=data)
        assert json.loads(web_request.text)['success']


    def back_matching_company(self,zhanzhuang_demand_id):
        #后台匹配展装公司
        data = {
            'bookId':zhanzhuang_demand_id,
            'DecoratorIdList[]':6532350
        }
        web_request = self.back_session.post(url=self.matching_company_url,data=data)
        assert json.loads(web_request.text)['success']

    def back_demand_contract_and_price(self,zhanzhuang_demand_id,price):
        #后台展装需求签合同及定价
        get_matching_company_data = {
            'bookId':zhanzhuang_demand_id,
            'page':1,
            'rows':20,
            'sort':'CreateOn',
            'order':'DESC'
        }
        web_request_get_zhanzhuang_company_num_id = self.back_session.get(url='http://back.zhankoo-uat.com/Exhibition/Decorate/DecorateBookDistributesFindPaged',data=get_matching_company_data)
        distributes_id = json.loads(web_request_get_zhanzhuang_company_num_id.text)['rows'][0]['ID']
        data = {
            'bookId':zhanzhuang_demand_id,
            'distributesId':distributes_id,
            'price':price,
            'isOffline':'false'
        }
        web_request = self.back_session.post(url=self.demand_contract_and_price_url,data=data)
        assert json.loads(web_request.text)['success']

    def back_finance_zhanzhuang_demand_price(self,zhanzhuang_demand_id):
        #后台财务提交展装需求定价
        data = {
            'bookId':zhanzhuang_demand_id,
            # 'page':1,
            # 'rows':20,
            # 'sort':'Order',
            # 'order':'ASC'
        }
        web_request = self.back_session.post(url=self.financ_zhanzhuang_demand_price_url,data=data)
        assert json.loads(web_request.text)['success']

    def zhanzhuang_demand_place_order(self,zhanzhuang_demand_id):
        #展装需求下订单
        data = {
            'DecorateBookID':zhanzhuang_demand_id,
            'InternatType':86,
            'CountryName':'中国',
            'CountryCode':86,
            'X-Requested-With':'XMLHttpRequest'
        }
        web_request = self.canzhanshang_session.post(url=self.zhanzhuang_demand_place_order_url,data=data)
        assert json.loads(web_request.text)['success']



