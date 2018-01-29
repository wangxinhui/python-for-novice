# 存储数据
# json.load 和 json.dump
import json
number="123"
number1="123"
l = ['iplaypython',[1,2,3], {'name':'xiaoming'}]
filename= 'json/numbers.json'
# with open(filename,'r+') as f_obj:
#     enjson = json.dumps(l)
#     dejson = json.loads(enjson)
#     print((enjson))


with open(filename,"r") as f_obj1:
    num = json.load(f_obj1)
    print(num)