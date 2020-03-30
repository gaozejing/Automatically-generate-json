import os
import random_fields as RF
import random_string as RS

count = 3
path = os.path.abspath('.')
key_list = ["user_name","age","phone_number","idcard","hardid",
            "education","gender","marriage","income"]

def value():
    return [RF.Chinese_name(), RF.age(), RF.phone_number(),RF.get_idnum(),RS.letter_string_case_insensitive(10),
            RF.get_education(),RF.get_sex(),RF.get_marriage(),RS.num_string(5)]