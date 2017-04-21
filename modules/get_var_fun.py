from modules.login import Login
from bs4 import BeautifulSoup
import re
import json

class Get_Var_Fun:

    zhubanfang_session = Login().send_login_request(name=18165702795,password=123456)
    back_session = Login().send_back_login_request()

    def zhubanfang_zhanhui_liebiao_var(self):
        #主办方展会列表
        url = 'http://exh.zhankoo-uat.com/Exhibition/Partial/_ListPage'
        data = {
            'pageIndex':1,
            'pageSize':10,
            'FromOn':'',
            'ToOn':'',
            'Name':''
        }
        web_request = self.zhubanfang_session.post(url=url,data=data)
        soup = BeautifulSoup(web_request.text,'lxml')
        exhibition_name = re.findall(r'"_blank">(.+?.)</a>',str(soup.select('td.txtleft a')[0]))[0]  #主办方列表展会名称
        exhibition_id = re.findall(r'(\d.*).html"',str(soup.select('td.txtleft a')[0]))[0]  #主办方列表展会ID
        return exhibition_name,exhibition_id

    def back_dajianshang_guangli_var(self):
        designer_find_paged_url = 'http://back.zhankoo-uat.com/AMemeber/User/DesignerFindPaged'
        data = {
            'UserID':'',
            'page':1,
            'rows':20,
            'sort':'Order',
            'order':'ASC'
        }
        web_request = self.back_session.post(url=designer_find_paged_url,data=data)
        designer_rows = json.loads(web_request.text)['rows']
        designer_list = []  #后台设计师ID列表
        for designer_rows_for in designer_rows:
            designer_list.append(designer_rows_for['ID'])
        return designer_list


if __name__ == '__main__':
    Get_Var_Fun().back_dajianshang_guangli_var()
