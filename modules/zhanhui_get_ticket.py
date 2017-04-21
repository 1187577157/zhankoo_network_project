from modules.login import Login
import requests
import json
from bs4 import BeautifulSoup
import re

class get_ticket:

    canzhanshang_session = Login().send_login_request(name=13690769964,password=123456)
    zhubanfang_session = Login().send_login_request(name=18165702795,password=123456)

    def get_ticket(self,exhibition_id):
        #获取展会门票
        ticket_lxml_url = 'http://exh.zhankoo-uat.com//exhibition/partial/_DetailActivityRegister?organizorID=12880853&eID=%s'% exhibition_id
        get_ticket_url = 'http://exh.zhankoo-uat.com/Exhibition/Home/ActivityRegisterSave'
        web_request_ticket = requests.get(url=ticket_lxml_url)
        soup = BeautifulSoup(web_request_ticket.text, 'lxml')
        ticket_active_id = soup.select('input')[0].get('value')
        ticket_name = soup.select('input')[0].get('title')
        from_on = soup.select('input')[0].get('data-from')
        to_on = soup.select('input')[0].get('data-to')
        data = {
            'ExhibitionID':exhibition_id,
            'TicketActiveID':ticket_active_id,
            'TicketName':ticket_name,
            'FromOn':from_on,
            'ToOn':to_on,
            'OrganizorID':'12880853',
            'RealName':'测试',
            'EnterpriseName':'深圳展酷网络有限公司',
            'Title':'test',
            'X-Requested-With':'XMLHttpRequest'
        }
        web_request =self.canzhanshang_session.post(url=get_ticket_url,data=data)
        assert json.loads(web_request.text)['success']

    def update_ticket_pass(self):
        #主办方审核通过展会门票
        organizer_ticket_page_url = 'http://exh.zhankoo-uat.com/Exhibition/Partial/_OrganizerTicketPage'
        organizer_ticket_page_data = {
            'pageIndex':1,
            'pageSize':20,
            'State':'所有状态'
        }
        web_request_organizer_ticket_page = self.zhubanfang_session.post(url=organizer_ticket_page_url,data=organizer_ticket_page_data)
        ticket_id = str(BeautifulSoup(web_request_organizer_ticket_page.text,'lxml')('a')[0])[51:56]
        update_ticket_pass_url = 'http://exh.zhankoo-uat.com/Exhibition/Organizer/UpdateTicketPass'
        data = {
            'ticketID':ticket_id,
            'checkOpinion':''
        }
        web_request = self.zhubanfang_session.post(url=update_ticket_pass_url,data=data)
        assert json.loads(web_request.text)['success']


if __name__ == '__main__':
    get_ticket().update_ticket_pass()