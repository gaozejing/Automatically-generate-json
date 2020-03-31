import random_string as RS
import random
from utils.langconv import Converter
from list_data import province_id,first_name,gender,education,marriage,phone_number_third
import socket
import struct

def get_age():
    '''
    随机生成0-100的年龄
    '''
    return random.randint(0,100)

def get_Eglish_name():
    '''
    随机生成英文名
    '''
    return RS.letter_string_capital(1)+RS.letter_string_lowercase(random.randint(2,10))

def get_phone_number():
    '''
    随机生成手机号
    '''
    return random.choice(phone_number_third) + RS.num_string(8)

def get_Chinese_name():
    '''
    随机生成中文名
    '''
    name_code = ''
    name_code+=random.choice(first_name)
    ran_num = random.randint(0,1)
    # 为0生成的名字是两个字,为1生成的名字是一个字
    if ran_num ==0:
        for i in range(2):
            # 从十进制汉字编码随机选取一个
            ran = random.randint(19968,40869)
            # 将其转换为汉字
            ran = chr(ran)
            name_code+=ran
    else:
        # 从十进制汉字编码随机选取一个
        ran = random.randint(19968, 40869)
        # 将其转换为汉字
        ran = chr(ran)
        name_code += ran
    # 将name_code里面的繁体字转换为简体字
    name_code = Converter('zh-hans').convert(name_code)
    # 编码
    name_code.encode('utf-8')
    return name_code

def get_idnum():
    '''
    随机生成身份证号
    '''
    id_num = ''
    # 随机选择地址码
    id_num += str(random.choice(province_id))
    # 随机生成4-6位地址码
    id_num += RS.num_string(4)
    #生成生日码
    id_num += get_birthday()
    # 生成15、16位顺序号
    id_num += RS.num_string(2)
    # 通过性别判断生成第十七位数字 男单 女双
    s = get_sex()
    if s =='男':
        # 生成奇数
        seventeen_num = random.randrange(1,9,2)
    else:
        seventeen_num = random.randrange(2,9,2)
    id_num+=str(seventeen_num)
    eighteen_num = str(random.randint(1,10))
    if eighteen_num =='10':
        eighteen_num = 'X'
    id_num+=eighteen_num
    return id_num

def get_birthday():
    '''
    随机生成出生日期
    '''
    year = random.randint(1920,2020)
    month = random.randint(1,12)
    # 判断每个月有多少天随机生成日
    if year%4 ==0:
        if month in (1,3,5,7,8,10,12):
            day = random.randint(1,31)
        elif month in (4,6,9,11):
            day = random.randint(1,30)
        else:
            day = random.randint(1,29)
    else:
        if month in (1,3,5,7,8,10,12):
            day = random.randint(1,31)
        elif month in (4,6,9,11):
            day = random.randint(1,30)
        else:
            day = random.randint(1,28)
    # 小于10的月份前面加0
    if month < 10:
        month = '0' + str(month)
    if day < 10:
        day = '0' + str(day)
    birthday = str(year)+str(month)+str(day)
    return birthday

# 性别
def get_sex():
    return random.choice(gender)

#学历
def get_education():
    return  random.choice(education)

#婚姻情况
def get_marriage():
    return random.choice(marriage)

def get_email():
    '''
    随机生成邮箱
    '''
    email = ''
    return email + RS.letter_string_case_insensitive(5) + '@' + RS.num_string(3) + '.com'

RANDOM_IP_POOL=['192.168.10.222/0']
def get_ip():
    '''
    随机生成ip地址
    '''
    str_ip = RANDOM_IP_POOL[random.randint(0, len(RANDOM_IP_POOL) - 1)]
    str_ip_addr = str_ip.split('/')[0]
    str_ip_mask = str_ip.split('/')[1]
    ip_addr = struct.unpack('>I',socket.inet_aton(str_ip_addr))[0]
    mask = 0x0
    for i in range(31, 31 - int(str_ip_mask), -1):
        mask = mask | ( 1 << i)
    ip_addr_min = ip_addr & (mask & 0xffffffff)
    ip_addr_max = ip_addr | (~mask & 0xffffffff)
    return socket.inet_ntoa(struct.pack('>I', random.randint(ip_addr_min, ip_addr_max)))


if __name__ == '__main__':
    for i in range(10):
        print(get_phone_number())