import random_fields as RF
import random_string as RS
import os
import write_data as WD




def create_json(count:int):
    with open(WD.path+'\\test.json',"w+",encoding="utf-8") as f:
        for j in range(count):
            f.write("{")
            for i in range(len(WD.key_list)):
                f.write('"%s":' % WD.key_list[i])
                f.write('"%s"' % WD.value()[i])
                if i<len(WD.key_list)-1:
                    f.write(",")
            f.write("}\n")

if __name__ == '__main__':
    create_json(2)

