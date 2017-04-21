import requests
import json

class CanZhanBao:
    #参展宝预定展位、展装服务

    book_zhanwei_insert_url = 'http://exh.zhankoo-uat.com/Home/BoothBookInsert'
    book_zhnawei_suppplement_url = 'http://exh.zhankoo-uat.com/Home/BoothBookSupplement'
    book_zhanzhuang_insert_url = 'http://exh.zhankoo-uat.com/Home/DecorateBookInsert'
    book_zhanzhuang_suppplement_url = 'http://exh.zhankoo-uat.com/Home/DecorateBookSupplement'

    def book_zhanwei(self,param):
        #预定展位
        insert_data = {
            'Contact':param['contact'],
            'Mobile':param['mobil'],
            'FromSite':param['from_site'],
            'FromSiteLocation':param['from_site_location']
        }
        web_request = requests.post(url=self.book_zhanwei_insert_url,data=insert_data)
        res = json.loads(web_request.text)['success']
        id = json.loads(web_request.text)['id']

        supplement_data = {
            'ID':id,
            'Enterprise':param['enterprise'],
            'MainProduct':param['main_product'],
            'IsFirstExhibit':param['is_first_exhibit'],
            'IntentCity':param['intent_city'],
            'ExhibitOn':param['exhibiti_on'],
            'RequireArea':param['require_area'],
            'IntentExhibition':param['intent_exhibition'],
            'X-Requested-With':'XMLHttpRequest'
        }
        web_request = requests.post(url=self.book_zhnawei_suppplement_url,data=supplement_data)
        res = json.loads(web_request.text)['success']
        assert res == True

    def book_zhanzhuang(self,param):
        #预定展装服务
        insert_data = {
            'Contact': param['contact'],
            'Mobile': param['mobil'],
            'FromSite': param['from_site'],
            'FromSiteLocation': param['from_site_location']
        }
        web_request = requests.post(url=self.book_zhanzhuang_insert_url, data=insert_data)
        res = json.loads(web_request.text)['success']
        id = json.loads(web_request.text)['id']
        assert res == True

        supplement_data = {
            'ID':id,
            'ServiceItem':param['service_item'],
            'ExhibitionName':param['exhibition_name'],
            'BoothArea':param['tooth_area'],
            'FinishOn':param['finish_on'],
            'Budget':param['budget'],
            'Enterprise':param['enterprise'],
            'X-Requested-With':'XMLHttpRequest'
        }
        web_request = requests.post(url=self.book_zhanzhuang_suppplement_url,data=supplement_data)
        res = json.loads(web_request.text)['success']
        assert res == True