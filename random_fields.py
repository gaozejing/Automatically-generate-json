import random_string as RS
import random

def age():
    return random.randint(0,100)

def Eglish_name():
    return RS.letter_string_capital(1)+RS.letter_string_lowercase(random.randint(2,10))

def phone_number():
    return '1'+ RS.num_string(10)

