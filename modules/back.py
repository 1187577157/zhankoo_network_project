import json
from modules.login import Login
from bs4 import BeautifulSoup

class Back:
    #运营后台数据
    zhanzhuang_xuqiu_url = 'http://back.zhankoo-uat.com/Exhibition/Decorate/DecorateBookFindPaged'
    zhanzhuang_dingdan_url = 'http://back.zhankoo-uat.com/SOrder/DecorateOrder/DecorateOrderFindPaged'
    zhanhui_xuqiu_url = 'http://back.zhankoo-uat.com/Exhibition/Booth/BoothBookFindPaged'
    zhanwei_dingdan_url = 'http://back.zhankoo-uat.com/SOrder/BoothOrder/BoothOrderFindPaged'
    zhanzhuang_gongchang_dingdan_url = 'http://back.zhankoo-uat.com/SOrder/DecFactoryOrder/DecFactoryOrderFindPaged'
    zhanhui_guangli_url = 'http://back.zhankoo-uat.com/Exhibition/Exhibition/ExhibitionFindPaged'
    del_zhanzhuang_xuqiu_url = 'http://back.zhankoo-uat.com/Exhibition/Decorate/DecorateBookDelete'
    del_zhanzhuang_dingdan_url = 'http://back.zhankoo-uat.com/SOrder/DecorateOrder/DecorateOrderDelete'
    del_zhanhui_xuqiu_url = 'http://back.zhankoo-uat.com/Exhibition/Booth/BoothBookDelete'
    del_zhanwei_dingdan_url = 'http://back.zhankoo-uat.com/SOrder/BoothOrder/BoothOrderDelete'
    del_zhanzhuang_gongchang_dingdan_url = 'http://back.zhankoo-uat.com/SOrder/DecFactoryOrder/DecFactoryOrderDelete'
    session = Login().send_back_login_request()

    '''
    1.展装需求
    2.展装订单
    3.展会需求
    4.展位订单
    5.展装工厂订单
    6.展会管理
    '''

    def back_management_list(self,code):
        #获取订单管理的id
        data = {
            'page':1,
            'rows':1,
            'sort':'CreateOn',
            'order':'DESC'
        }
        if code == 1:
            url = self.zhanzhuang_xuqiu_url
        elif code == 2:
            url = self.zhanzhuang_dingdan_url
        elif code == 3:
            url = self.zhanhui_xuqiu_url
        elif code == 4:
            url = self.zhanwei_dingdan_url
        elif code == 5:
            url = self.zhanzhuang_gongchang_dingdan_url
        elif code ==6:
            url = self.zhanhui_guangli_url
        web_request = self.session.post(url,data=data)
        id = json.loads(web_request.text)['rows'][0]['ID']
        return id

    def back_del_management_list_data(self,id,code):
        #删除订单管理数据
        data = {
            'id':id
        }
        if code == 1:
            url = self.del_zhanzhuang_xuqiu_url
        elif code == 2:
            url = self.del_zhanzhuang_dingdan_url
        elif code == 3:
            url = self.del_zhanhui_xuqiu_url
        elif code == 4:
            url = self.del_zhanwei_dingdan_url
        elif code == 5:
            url = self.del_zhanzhuang_gongchang_dingdan_url
        elif code == 6:
            url = self.zhanhui_guangli_url
        web_request = self.session.post(url,data=data)
        res = json.loads(web_request.text)['success']
        return res == True

    def back_booth_order_detials(self,order_id):
        #后台展位订单详情
        booth_basics_info_url = 'http://back.zhankoo-uat.com/SOrder/BoothOrder/BoothOrderDetailView/%s'% order_id
        web_request_booth_basics_info = self.session.get(url=booth_basics_info_url)
        soup1 = BeautifulSoup(web_request_booth_basics_info.text, 'lxml')
        exhibition_name = str(soup1.select('td')[15])[4:-5]
        booth_info_url = 'http://back.zhankoo-uat.com/SOrder/BoothOrder/BoothSnapshotFindPaged'
        data = {
            'BoothOrderID':681,
            'page':1,
            'rows':20,
            'sort':'CreateOn',
            'order':'DESC'
        }
        web_request_booth_info = self.session.get(url=booth_info_url,data=data)
        booth_id = json.loads(web_request_booth_info.text)['rows'][0]['ID']
        booth_name = json.loads(web_request_booth_info.text)['rows'][0]['Name']
        # print(booth_name)

        return exhibition_name,booth_id,booth_name


if __name__ == '__main__':
    id = Back().back_management_list(code=4)
    Back().back_booth_order_detials(order_id=id)