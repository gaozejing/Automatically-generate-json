import os
import random_fields as RF
import random_string as RS

count = 2
path = os.path.abspath('.')
key_list = ["user_name","age","phone_number","idcard","hardid",
            "education","gender","marriage","income","email","user_id",
            "ip","const_id"]

def value():
    return [RF.get_Chinese_name(), RF.get_age(), RF.get_phone_number(),RF.get_idnum(),RS.letter_string_case_insensitive(10),
            RF.get_education(),RF.get_sex(),RF.get_marriage(),RS.num_string(5),RF.get_email(),RS.letter_and_number(6),
            RF.get_ip(),RS.letter_and_number(18)]