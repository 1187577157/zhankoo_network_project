import json
from bs4 import BeautifulSoup
from modules.login import Login
import os
import re

class New_Exhibition:
    '''新增展会信息'''
    basic_info_url = 'http://exh.zhankoo-uat.com/Exhibition/Organizer/BasicSave'
    exhibition_introduction_url = 'http://exh.zhankoo-uat.com/Exhibition/Organizer/IntroductionSave'
    organization_url = 'http://exh.zhankoo-uat.com/Exhibition/Organizer/InstitutionSave'
    basic_booth_url = 'http://exh.zhankoo-uat.com/Exhibition/Organizer/BasicBoothSave'
    exhibition_picture_upload_url = 'http://exh.zhankoo-uat.com/Exhibition/Organizer/ExPictureSave'
    exhibition_picture_url = 'http://exh.zhankoo-uat.com/Exhibition/Organizer/PictureSave'
    meeting_picture_upload_url = 'http://exh.zhankoo-uat.com/Exhibition/Organizer/MeetingPictureSave'
    meeting_url = 'http://exh.zhankoo-uat.com/Exhibition/Organizer/MeetingSave'
    contact_url = 'http://exh.zhankoo-uat.com/Exhibition/Organizer/ContactSave'
    exhibition_data_url = 'http://exh.zhankoo-uat.com/Exhibition/Organizer/DataSave'
    exhibitor_url = 'http://exh.zhankoo-uat.com/Exhibition/Organizer/ExhibitorSave'
    back_edit_exhibition_url = 'http://back.zhankoo-uat.com/Exhibition/Exhibition/ExhibitionSave'
    add_zhanwei_url = 'http://exh.zhankoo-uat.com/exhibition/organizer/onlineboothinsert'
    zhanwei_peizhi_xinxi_url = 'http://exh.zhankoo-uat.com/exhibition/organizer/onlineboothstandardboothconfigsave'
    zhanwei_picture_upload_url = 'http://exh.zhankoo-uat.com/Exhibition/Organizer/OnlineBoothPictureFrom'
    zhanwei_picture_url = 'http://exh.zhankoo-uat.com/exhibition/organizer/onlineboothpicturesave'
    update_exhibition_index_url = 'http://back.zhankoo-uat.com/CompositePlat/SearchEngine/UpdateAllExhibition'
    back_update_zhanhui_index_url = 'http://back.zhankoo-uat.com/CompositePlat/SearchEngine/UpdateAllExhibition'
    zhubanfang_session = Login().send_login_request(name=18165702795,password=123456)
    back_session = Login().send_back_login_request()

    def new_basic_info(self,param):
        '''新增基本信息'''
        data = {
            'ID':0,
            'Name':param['name'],
            'ShortName':'测试',
            'IndustryName':param['industry_name'],
            'IndustryID':param['industry_id'],
            'ExhibitCategory':'[{"ID":3,"Name":"包装机械/塑料机械"},{"ID":62,"Name":"门窗"}]',
            'HoldFrequencyWithYear':1,
            'HoldFrequency':1,
            'FromOn':param['from_on'],
            'ToOn':param['to_on'],
            'PavilionID':3118,
            'PavilionName':'深圳会展中心',
            'Address':'中国广东深圳市福田区',
            'Site':'www.zhankoo.com',
            'X-Requested-With':'XMLHttpRequest'
        }
        web_request = self.zhubanfang_session.post(url=self.basic_info_url,data=data)
        soup = BeautifulSoup(web_request.text,'lxml')
        result = soup.select('html > body > p')[0].get_text()
        return json.loads(result)

    def new_zhanhui_introduction(self,exhibition_id,description,scope,label):
        '''新增展会介绍'''
        data = {
            'ID':exhibition_id,
            'Description':description,
            'Scope':scope,
            'ExhibitorManualUrl':'',
            'Tag':label,
            'X-Requested-With':'XMLHttpRequest'
        }
        web_request = self.zhubanfang_session.post(url=self.exhibition_introduction_url,data=data)
        assert json.loads(web_request.text)['success']

    def new_organization(self,exhibition_id,organizer,contractor):
        '''新增举办机构'''
        data = {
            'ID':exhibition_id,
            'Organizer':organizer,
            'Contractor':contractor,
            'X-Requested-With':'XMLHttpRequest'
        }
        web_request = self.zhubanfang_session.post(url=self.organization_url,data=data)
        assert json.loads(web_request.text)['success']

    def new_booth_info(self,exhibition_id,param):
        '''新增展位基本信息'''
        orderjson_data = [
                {'Type':1,
                'Price':param['biaozhan_price'],
                'Area':param['biaozhan_area'],
                'Description':param['biaozhan_description']},
                {'Type':2,
                'Price': param['guangdi_price'],
                'Area': param['guangdi_area'],
                'Description': param['guangdi_description']}]
        data = {
            'ID':exhibition_id,
            'MinOrderJson':str(orderjson_data),
            'StandardBoothMoney':param['biaozhan_price'],
            'StandardBoothArea':param['biaozhan_area'],
            'StandardBoothRemark':param['biaozhan_description'],
            'BareSpaceBoothMoney':param['guangdi_price'],
            'BareSpaceBoothArea':param['guangdi_area'],
            'BareSpaceBoothRemark':param['guangdi_description'],
            'X-Requested-With': 'XMLHttpRequest'
        }
        web_request = self.zhubanfang_session.post(url=self.basic_booth_url,data=data)
        assert json.loads(web_request.text)['success']

    def picture_upload(self, index, filename):
      #index == 1 为上传展会图片，index == 2 为上传同期会议图片
        current = os.getcwd()
        base = current.split('\\test_case')[0]
        target = base + '\\data_file\\' + filename
        open_file = {'file': open(target, 'rb')}
        url = ''
        if index == 1:
            url = self.exhibition_picture_upload_url
        elif index == 2:
            url = self.meeting_picture_upload_url
        elif index ==3:
            url = self.zhanwei_picture_upload_url
        web_response = self.zhubanfang_session.post(url=url, files=open_file)
        result = ''
        if index == 1:
            result = json.loads(web_response.text.split('OnCompleteUpload')[1].split('catch(e)')[0][2:-4])
        elif index == 2:
            result = json.loads(web_response.text.split('MeetingComplete')[1].split('catch(e)')[0][2:-4])
        elif index == 3:
            result = json.loads(web_response.text.split('OnCompleteUpload')[1].split('catch(e)')[0][2:-4])
        assert result['success'] == True
        return result['pictureUrl']

    def save_exhibition_picture(self,exhibition_id,imges):
        #保存展会图片
        data = {
            'ID': exhibition_id,
            'ImgStr': imges
        }
        web_request = self.zhubanfang_session.post(url=self.exhibition_picture_url, data=data)
        assert json.loads(web_request.text)['success']

    def new_meeting(self,exhibition_id,param):
        #新增同期会议
        data = {
            'ID':'',
            'ExhibitionID':exhibition_id,
            'Name':param['meeting_title'],
            'MeetingFromOn':param['meeting_from_on'],
            'MeetingToOn':param['meeting_to_on'],
            'Address':param['address'],
            'Organizer':param['organizer'],
            'MaxPeople':param['max_people'],
            'ImageUrl':param['image-url'],
            'Description':param['descrition'],
            'X-Requested-With':'XMLHttpRequest'
        }
        web_request = self.zhubanfang_session.post(url=self.meeting_url, data=data)
        assert json.loads(web_request.text)['success']

    def contact_info(self,exhibition_id,param):
        #新增联系方式
        data = {
            'ID':exhibition_id,
            'Contact':param['contact'],
            'Telephone':param['telephone'],
            'Mobile':param['mobile'],
            'Fax':param['fax'],
            'QQ':param['qq'],
            'Email':param['email'],
            'X-Requested-With':'XMLHttpRequest'
        }
        web_request = self.zhubanfang_session.post(url=self.contact_url, data=data)
        assert json.loads(web_request.text)['success']

    def new_exhibition_data(self,exhibition_id,param):
        #新增展会数据
        audiences_data = [{"Id": "0", "Statue": "new", "Type": param['textfield_type_1'], "Percent": param["textfield_percent_1"]},
                          {"Id": "0", "Statue": "new", "Type": param['textfield_type_2'],"Percent":param["textfield_percent_2"]}]
        exhibitors_data = [{"Id": "0", "Statue": "new", "Type": param['textfield_type_3'], "Percent": param["textfield_percent_3"]},
                           {"Id": "0", "Statue": "new","Type":param['textfield_type_4'],"Percent":param["textfield_percent_4"]}]
        data = {
            'ExhibitionID':exhibition_id,
            'Area':param['area'],
            'NetArea':param['net_area'],
            'HistoryNum':param['history_num'],
            'ViewerQuantity':param['viewer_quantity'],
            'id':0,
            'statue':'new',
            'textfield3':param['textfield_type_1'],
            'textfield6':param['textfield_percent_1'],
            'AudiencesData':str(audiences_data),
            'id':0,
            'statue':'new',
            'textfield3':param['textfield_type_2'],
            'textfield6':param['textfield_percent_2'],
            'ExhibitorQuantity':param['exhibition_quantity'],
            'id':0,
            'statue':'new',
            'textfield3':param['textfield_type_3'],
            'textfield6':param["textfield_percent_3"],
            'id':0,
            'statue':'new',
            'textfield3':param['textfield_type_4'],
            'textfield6':param['textfield_percent_4'],
            'ExhibitorsData':str(exhibitors_data),
            'ViewerSatisfy':param['viewer_satisfy'],
            'ExhibitorSatisfy':param['exhibitor_satisfy'],
            'X-Requested-With':'XMLHttpRequest'
        }
        web_request = self.zhubanfang_session.post(url=self.exhibition_data_url, data=data)
        assert json.loads(web_request.text)['success']

    def new_exhibitor(self,exhibition_id,exhibitor_list):
        #新增展商名录
        data = {
            'ID':exhibition_id,
            'ExhibitorList':exhibitor_list,
            'X-Requested-With':'XMLHttpRequest'
        }
        web_request = self.zhubanfang_session.post(url=self.exhibitor_url, data=data)
        assert json.loads(web_request.text)['success']

    def back_edit_zhanhui(self,exhibition_id):
        # 后台编辑审核、签约展会信息
        request_back_get_edit_zhanhui_data = self.back_session.post(url='http://back.zhankoo-uat.com/Exhibition/Exhibition/ExhibitionDetailView/%s'% exhibition_id)
        soup = BeautifulSoup(request_back_get_edit_zhanhui_data.text,'lxml')
        exhibition_id = soup.select('td')[1]('input')[0].get('value')
        name = soup.select('td')[1]('input')[1].get('value')
        short_name = soup.select('td')[3]('input')[0].get('value')
        pavilion_name = soup.select('td')[15]('input')[0].get('value')
        pavilion_id = soup.select('td')[15]('input')[1].get('value')
        organizer = re.findall(r'">(.+?.)</textarea>',str(soup.select('td')[17]))[0]
        contractor = re.findall(r'">(.+?.)</textarea>',str(soup.select('td')[19]))[0]
        scope = re.findall(r'">(.+?.)</textarea>',str(soup.select('td')[21]))[0]
        description = re.findall(r'">(.+?.)</textarea>',str(soup.select('td')[23]))[0]
        from_on = re.findall(r'value:\'(.+?.)\'',str(soup.select('td')[25]('input')[0]))[0]
        to_on = re.findall(r'value:\'(.+?.)\'',str(soup.select('td')[25]('input')[1]))[0]
        ticket_end_on = re.findall(r'value:\'(.+?.)\'',str(soup.select('td')[27]))[0]
        book_end_on = re.findall(r'value:\'(.+?.)\'',str(soup.select('td')[29]))[0]
        site = soup.select('td')[35]('input')[0].get('value')
        industry_id = re.findall(r'value:\'(\d*)\'',str(soup.select('td')[43]('input')[0]))[0]
        industry_name= soup.select('td')[43]('input')[1].get('value')
        exhibit_category = soup.select('td')[45]('input')[0].get('value')
        tag = soup.select('td')[47]('input')[0].get('value')
        contact = soup.select('td')[49]('input')[0].get('value')
        internat_type = soup.select('td')[51]('input')[0].get('value')
        country_code = soup.select('td')[51]('input')[0].get('value')
        country_name = soup.select('td')[51]('input')[0].get('value')
        province_name = soup.select('td')[51]('input')[1].get('value')
        city_name = soup.select('td')[51]('input')[2].get('value')
        county_name = soup.select('td')[51]('input')[3].get('value')
        telephone = soup.select('td')[53]('input')[0].get('value')
        mobile = soup.select('td')[55]('input')[0].get('value')
        qq = soup.select('td')[57]('input')[0].get('value')
        fax = soup.select('td')[59]('input')[0].get('value')
        address = soup.select('td')[61]('input')[0].get('value')
        postalcode = soup.select('td')[63]('input')[0].get('value')
        email = soup.select('td')[65]('input')[0].get('value')
        min_order_json = soup.select('td')[73]('input')[0].get('value')
        booth_discount = soup.select('td')[75]('input')[0].get('value')
        standard_booth_config = str(soup.select('td')[81])[128:-16]
        area = soup.select('td')[83]('input')[0].get('value')
        net_area = soup.select('td')[85]('input')[0].get('value')
        hold_frequency = eval(soup.select('td')[87]('input')[0].get('value'))
        hold_year = hold_frequency['year']
        hold_boundary = hold_frequency['number']
        viewer_quantity = soup.select('td')[91]('input')[0].get('value')
        exhibitor_quantity = soup.select('td')[95]('input')[0].get('value')
        viewer_satisfy = soup.select('td')[99]('input')[0].get('value')
        exhibitor_satisfy = soup.select('td')[101]('input')[0].get('value')
        history_num = soup.select('td')[105]('input')[0].get('value')
        exhibitor_list = re.findall(r'">(.+?.)</textarea>',str(soup.select('td')[107]))[0]
        virtual_synthesize_goal = soup.select('td')[117]('input')[0].get('value')
        data = {
            'ID':exhibition_id,
            'Name':name,
            'ShortName':short_name,
            'PavilionName':pavilion_name,
            'PavilionID':pavilion_id,
            'Organizer':organizer,
            'Contractor':contractor,
            'Scope':scope,
            'Description':description,
            'FromOn':from_on,
            'ToOn':to_on,
            'TicketEndOn':ticket_end_on,
            'BookEndOn':book_end_on,
            'Site':site,
            'IsSign':'True',
            'IndustryID':industry_id,
            'IndustryName':industry_name,
            'ExhibitCategory':exhibit_category,
            'Tag':tag,
            'Contact':contact,
            'InternatType':internat_type,
            'CountryCode':country_code,
            'CountryName':country_name,
            'ProvinceName':province_name,
            'CityName':city_name,
            'CountyName':county_name,
            'Telephone':telephone,
            'Mobile':mobile,
            'QQ':qq,
            'Fax':fax,
            'Address':address,
            'Postalcode':postalcode,
            'Email':email,
            'State':1,
            'MinOrderJson':min_order_json,
            'BoothDiscount':booth_discount,
            'StandardBoothConfig':standard_booth_config,
            'Area':area,
            'NetArea':net_area,
            'HoldFrequency':hold_frequency,
            'HoldYear': hold_year,
            'HoldBoundary': hold_boundary,
            'ViewerQuantity':viewer_quantity,
            'ExhibitorQuantity':exhibitor_quantity,
            'ViewerSatisfy':viewer_satisfy,
            'ExhibitorSatisfy':exhibitor_satisfy,
            'HistoryNum':history_num,
            'ExhibitorList':exhibitor_list,
            'VirtualSynthesizeGoal':virtual_synthesize_goal
        }
        web_request = self.back_session.post(url=self.back_edit_exhibition_url,data=data)
        assert json.loads(web_request.text)['message'] == '操作成功！'

    def add_zhanwei(self,exhibition_id,param):
        #新增展位
        data = {
            'ExhibitionID':exhibition_id,
            'Name':param['zhanwei_num'],
            'PavilionNO':param['zhanguang_num'],
            'Type':param['zhanwei_xingshi'],
            'StandardType':param['kaikou_leixing'],
            'Price':param['price'],
            'Area':param['area'],
            'Length':param['length'],
            'Width':param['width'],
            'Discount':param['discount'],
            'IsSell':param['is_sell'],
           'Description':param['description']
        }
        web_request = self.zhubanfang_session.post(url=self.add_zhanwei_url,data=data)
        assert json.loads(web_request.text)['success']

    def zhanwei_peizhi_xinxi(self,exhibition_id,standard_booth_config):
        #新增展位配置信息
        data = {
            'StandardBoothConfig':standard_booth_config,
             'ID':exhibition_id
        }
        web_request = self.zhubanfang_session.post(url=self.zhanwei_peizhi_xinxi_url, data=data)
        assert json.loads(web_request.text)['success']

    def save_zhanwei_picture(self,exhibition_id,zhanwei_picture):
        #上传展位图片
        data = {
            'BoothImageUrl':zhanwei_picture,
            'ID':exhibition_id
        }
        web_request = self.zhubanfang_session.post(url=self.zhanwei_picture_url, data=data)
        assert json.loads(web_request.text)['success']

    def back_update_zhanhui_index(self):
        #后台更新展会索引
        web_request = self.back_session.post(url=self.back_update_zhanhui_index_url)
        assert json.loads(web_request.text)['success']


if __name__ == '__main__':
    New_Exhibition().back_edit_zhanhui(exhibition_id=29367)