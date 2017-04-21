import json
from bs4 import BeautifulSoup
from modules.login import Login
import random

class zhanhui_order:

    canzhanshang_session = Login().send_login_request(name=13690769964,password=123456)
    zhubanfang_session = Login().send_login_request(name=18165702795,password=123456)

    def online_booth_order(self,exhibition_id):
        #在线预订展位确认订单
        online_booth_book_url = 'http://exh.zhankoo-uat.com/Exhibition/Partial/_BoothBookPaged'
        online_booth_book_data = {
            'pageIndex':1,
            'pageSize':10,
            'exhibitionID':exhibition_id,
            'state':'1',
            'isSell':'null',
            'type':'',
            'standardType':'',
            'minArea':'',
            'maxArea':'',
            'minTotalPrice':'',
            'maxTotalPrice':'',
            'orderType':'null'
        }
        web_request_online_booth_book = self.canzhanshang_session.post(url=online_booth_book_url,data=online_booth_book_data)
        online_booth_book_soup = BeautifulSoup(web_request_online_booth_book.text,'lxml')
        result = online_booth_book_soup.select('tr')
        booth_id_list = []
        for for_result in result:
            booth_id_list.append(for_result.get('data-id'))
        booth_id_list.pop()
        return random.choice(booth_id_list)


    def booth_book_sure_order_save(self,exhibition_id,booth_id):
        #预定展位提交订单
        sure_order_url = 'http://exh.zhankoo-uat.com/exhibition/home/sureorder'
        sure_order_save_url = 'http://exh.zhankoo-uat.com/Exhibition/Home/SureOrderSave'
        sure_order_data = {
            'exhibitionid': exhibition_id,
            'boothids': booth_id
        }
        web_request_sure_order = self.canzhanshang_session.get(url=sure_order_url,data=sure_order_data)
        sure_order_soup = BeautifulSoup(web_request_sure_order.text,'lxml')
        original_price = sure_order_soup.select('input')[3]['value']
        total_price = sure_order_soup.select('input')[4]['value']
        sure_order_save_data = {
            'ExhibitionID':exhibition_id,
            'ContactID':134851,
            'ExhibitorEnterpriseID':519,
            'OriginalPrice':original_price,
            'TotalPrice':total_price,
            'CountryName':'中国',
            'BoothIDs':booth_id,
            'InternatType':86,
            'CountryCode':86,
            'X-Requested-With':'XMLHttpRequest'
        }
        web_request_sure_order_save = self.canzhanshang_session.post(url=sure_order_save_url,data=sure_order_save_data)
        order_id = json.loads(web_request_sure_order_save.text)['orderID']
        return order_id

    def canzhanshang_zhanhui_order_list(self):
        #展位订单列表
        canzhanshang_order_page = 'http://so.zhankoo-uat.com/Exhibition/Partial/_ExhibitorOrderPage'
        data = {
            'pageIndex':1,
            'pageSize':5,
            'exhibitionName':'',
            'createOnFrom':'',
            'state':0
        }
        web_request = self.canzhanshang_session.post(url=canzhanshang_order_page,data=data)
        print(BeautifulSoup(web_request.text,'lxml'))


    def organizer_comfirm_order(self,order_id):
        #主办方确认订单
        organizer_comfirm_order_url = 'http://so.zhankoo-uat.com/Exhibition/Organizer/OrderConfirm'
        data = {
            'stageCount':1,
            'orderID':order_id,
            'stageParam':'[]'
        }
        web_request = self.zhubanfang_session.post(url=organizer_comfirm_order_url,data=data)
        assert json.loads(web_request.text)['success']
#
#     def zhanhui_order_pay(self):
#         pay1_url = 'http://so.zhankoo-uat.com/Home/Pay?type=1&stageID=7148'
#         web_request_immediate_pay = self.canzhanshang_session.get(url=pay1_url)
#         orderStageID = json.loads(web_request_immediate_pay.text)['orderStageID']
#         amount = json.loads(web_request_immediate_pay.text)['amount']
#         code = json.loads(web_request_immediate_pay.text)['code']
#         type = json.loads(web_request_immediate_pay.text)['type']
#
#         pay2_url = 'http://pay.zhankoo-uat.com/roppay/index'
#         data1 = {
#             'type':type,
#             'orderStageID':orderStageID,
#             'amount':amount,
#             'productName':'展会订单支付',
#             'productDesc':'展会订单%s第%s期支付款'%(code,orderStageID),
#             'returnUrl':'//so.zhankoo-uat.com/exhibition/exhibitor/orderlist'
#         }
#         web_request2 = self.canzhanshang_session.post(url=pay2_url,data=data1)
#         soup1 = BeautifulSoup(web_request2.text,'lxml')
#         merchantNo = soup1.select('input')[0].get('value')
#         orderNo = soup1.select('input')[1].get('value')
#         productNo = soup1.select('input')[2].get('value')
#         productName = soup1.select('input')[3].get('value')
#         productDesc = soup1.select('input')[4].get('value')
#         productNum = soup1.select('input')[5].get('value')
#         orderAmount = soup1.select('input')[6].get('value')
#         amtType = soup1.select('input')[8].get('value')
#         pageUrl = soup1.select('input')[14].get('value')
#         notifyUrl = soup1.select('input')[15].get('value')
#         orderTime = soup1.select('input')[16].get('value')
#         orderMark = soup1.select('input')[18].get('value')
#         expand = soup1.select('input')[19].get('value')
#         expand2 = soup1.select('input')[20].get('value')
#         signType = soup1.select('input')[21].get('value')
#         busiCode = soup1.select('input')[22].get('value')
#         version = soup1.select('input')[23].get('value')
#         charset = soup1.select('input')[24].get('value')
#         signMsg = soup1.select('input')[25].get('value')
#
#         pay3_url = 'http://devrsjf.rongcapital.com.cn:8486/checkstand/payment'
#         data3 = {
#             'merchantNo':merchantNo,
#             'orderNo':orderNo,
#             'productNo':productNo,
#             'productName':productName,
#             'productDesc':productDesc,
#             'productNum':productNum,
#             'orderAmount':int(float(orderAmount)),
#             'payType':'',
#             'amtType':amtType,
#             'bankInfo':'',
#             'payerAcount':'',
#             'payerName':'',
#             'payerPhone':'',
#             'payerMail':'',
#             'pageUrl':pageUrl,
#             'notifyUrl':notifyUrl,
#             'orderTime':orderTime,
#             'orderExpireTime':'',
#             'orderMark':orderMark,
#             'expand':expand,
#             'expand2':expand2,
#             'signType':signType,
#             'busiCode':busiCode,
#             'version':version,
#             'charset':charset,
#             'signMsg':signMsg
#         }
#         web_reuqest3 = self.canzhanshang_session.post(url=pay3_url,data=data3)
#         print(BeautifulSoup(web_reuqest3.text,'lxml'))
#
#
# if __name__ == '__main__':
#     zhanhui_order().zhanhui_order_pay()
#



