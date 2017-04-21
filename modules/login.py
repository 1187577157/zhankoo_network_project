import requests
from bs4 import BeautifulSoup
import json

class Login:
#展酷网登录
    login_page_url = 'http://passport.zhankoo-uat.com/account/login/'
    login_url = 'http://passport.zhankoo-uat.com/Account/LoginAjax'
    back_login_url = 'http://back.zhankoo-uat.com/account/signin'

    def get_login_token(self):
        #返回登录token
        web_response = requests.get(self.login_page_url)
        soup = BeautifulSoup(web_response.text, 'lxml')
        token = soup.find('input', attrs={'name': '__RequestVerificationToken'}).get('value')
        return token

    def send_login_request(self,name=18165702795,password=123456):
        #展酷网前台登录
        session =requests.session()
        token = self.get_login_token()
        data = {
            '__RequestVerificationToken':token,
            'LoginFailNum':1,
            'Name':name,
            'Password':password,
            'VerifyCode':'',
            'RememberMe':'false',
            'X-Requested-With':'XMLHttpRequest'
        }
        web_request = session.post(self.login_url,data=data)
        soup = BeautifulSoup(web_request.text,'lxml')
        result = soup.select('body > p')[0].get_text()
        return session

    def send_back_login_request(self,login_name='admin_default@izhanxiao.com',password='zkadmin_987456'):
        #展酷网后台登录
        session = requests.session()
        data = {
            'loginName':login_name,
            'password':password
        }
        session.post(url=self.back_login_url,data=data)
        return session


if __name__ == '__main__':
    print(Login().send_back_login_request())

