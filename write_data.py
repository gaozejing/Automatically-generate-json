import os
import random_fields as RF

path = os.path.abspath('.')
key_list = ["user_name","age","phone_number"]

def value():
    return [RF.Eglish_name(), RF.age(), RF.phone_number()]