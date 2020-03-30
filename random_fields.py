import random_string as RS
import random
import firstname
from langconv import Converter
from province_id import province_id

def age():
    '''
    随机生成0-100的年龄
    :return:
    '''
    return random.randint(0,100)

def Eglish_name():
    '''
    随机生成英文名
    :return:
    '''
    return RS.letter_string_capital(1)+RS.letter_string_lowercase(random.randint(2,10))

def phone_number():
    '''
    随机生成手机号
    :return:
    '''
    return '1'+ RS.num_string(10)

def Chinese_name():
    '''
    随机生成中文名
    :return:
    '''
    name_code = ''
    name_code+=random.choice(firstname.first_name)
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
    :return:
    '''
    id_num = ''
    # 随机选择地址码
    id_num+=str(random.choice(province_id))
    # 随机生成4-6位地址码
    for i in range(4):
        ran_num = str(random.randint(0,9))
        id_num+=ran_num
    b = get_birthday()
    id_num+=b
    # 生成15、16位顺序号
    num = ''
    for i in range(2):
        num += str(random.randint(0,9))
    id_num+=num
    # 通过性别判断生成第十七位数字 男单 女双
    s = get_sex()
    print("性别:",s)
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
    随机生成出售日期
    :return:
    '''
    # 随机生成年月日
    year = random.randint(1960,2000)
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

# 匿名函数性别
get_sex = lambda :random.choice(['男','女'])