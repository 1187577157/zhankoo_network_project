import xlrd
import os

#获取excel的数据
def get_default_file_path():
    current_path = os.getcwd()
    base = current_path.split('\\test_case')[0]
    path = base + '\\data_file\\zhankoo_data.xlsx'
    return path

def open_excel(file):
    data = xlrd.open_workbook(file)
    return data

def excel_table_by_index(file=get_default_file_path(),by_index=0):
    data = open_excel(file)
    table = data.sheets()[by_index]
    nrows = table.nrows
    data_list = []
    for rownum in range(nrows):
        row = table.row_values(rownum)
        data_list.append(row)
    return data_list

if __name__ == '__main__':
    excel_table_by_index()
