# 写入文件
import codecs

# files = codecs.open("files/write_file.txt", "a", "utf-8")
# files.write("你好\n")
# files.write("hello Python \n")
# 打开文件时，可指定读取模式 （'r' ）、写入模式 （'w' ）、附加模式 （'a' ）或让你能够读取
# 和写入文件的模式（'r+' ）。如果你省略了模式实参，Python将以默认的只读模式打开文件。
# 基本的写入文件
# with open("files/write_file.txt", "a") as write_file:
#     str_en = "hello Python"
#     write_file.write(str_en + "\n")


# username = input("input your name please:")
# username_file = codecs.open("files/username.txt","w","utf-8")
# if username != '':
#     username_file.write(username+"\n")
#
# print("your name were record in my system")

novice_list = ['惊心动魄的一幕结束','黄叶在秋风中飘落结束','在困难的日子里结束',
               '你怎么也想不到结束','我和五叔的六次相遇结束','人生结束',
               '人生-文学剧本结束','早晨从中午开始结束','匆匆过客结束','姐姐结束',
               '卖猪结束','青松与小红花结束','痛苦结束','我为我心爱的人儿结束',
               '路遥文集夏结束','小镇上结束','杏树下结束','一生中最高兴的一天结束',
               '医院里结束','月夜静悄悄结束','生活咏叹调结束','病危中的柳青结束']

with open("files/novice.txt",encoding='utf-8') as f_obj:
    contexts = f_obj.readlines()
    novice_single = ""
    for line in contexts:
        novice_single += line
        for novice in novice_list:
            if line.rstrip() == novice:
                with open("files/"+novice[0:-2]+".txt","w",encoding='utf-8') as new_obj:
                    new_obj.write(novice_single)
                novice_single = ""