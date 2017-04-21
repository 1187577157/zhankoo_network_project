import requests
from bs4 import BeautifulSoup
import re
import json

class zhanhui_search:

    def zhanhui_search(self,keyword):
        #展会搜索
        zhanhui_search_url = 'http://exh.zhankoo-uat.com/zhanhui?keyword=%s'%keyword
        web_request = requests.post(url=zhanhui_search_url)
        soup = BeautifulSoup(web_request.text,'lxml')
        search_result = soup.select('div.content a')[0].get('title')
        assert re.findall(search_result,keyword)



if __name__ == '__main__':
    zhanhui_search().zhanhui_search(keyword='测试')