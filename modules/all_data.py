import random
import string
from random import Random

def all_str_data():
    #随机字符串
    chinese_char = "".join(map(chr, range(0x4E00, 0x9FBF)))
    chars ='AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789\'`~!@#$%^&*()_+=-\][{}|;":?></.,'
    all_str_data =chinese_char + chars
    random_all_str= random.sample(all_str_data,21000)
    return  random_all_str



if __name__ == '__main__':
    print(all_str_data())
