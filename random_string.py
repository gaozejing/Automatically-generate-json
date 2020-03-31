import random

def num_string(count:int):
    '''
    纯数字字符串
    :param count: 字符串长度
    :return:
    '''
    num_str = ''
    for i in range(0,count):
        num = random.randint(0,9)
        num_str += str(num)
    return num_str

def letter_string_case_insensitive(count:int):
    '''
    不区分大小写的纯字母字符串
    :param count: 字符串长度
    :return:
    '''
    H = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    letter_str = ''
    for i in range(0,count):
        letter = random.choice(H)
        letter_str += letter
    return letter_str

def letter_string_lowercase(count:int):
    '''
    仅小写的纯字母字符串
    :param count: 字符串长度
    :return:
    '''
    H = 'abcdefghijklmnopqrstuvwxyz'
    letter_str = ''
    for i in range(0,count):
        letter = random.choice(H)
        letter_str += letter
    return letter_str

def letter_string_capital(count:int):
    '''
    仅大写的纯字母字符串
    :param count: 字符串长度
    :return:
    '''
    H = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    letter_str = ''
    for i in range(0,count):
        letter = random.choice(H)
        letter_str += letter
    return letter_str

def letter_and_number(count:int):
    '''
    大小写字母+数字
    :param count:
    '''
    H = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
    lan_str = ''
    for i in range(0,count):
        lan = random.choice(H)
        lan_str += lan
    return lan_str

def bool():
    return random.choice(['true','false'])

if __name__ == '__main__':
    print((3))