# 写入文件
import codecs

files = codecs.open("files/write_file.txt", "a", "utf-8")
files.write("你好\n")
# 打开文件时，可指定读取模式 （'r' ）、写入模式 （'w' ）、附加模式 （'a' ）或让你能够读取
# 和写入文件的模式（'r+' ）。如果你省略了模式实参，Python将以默认的只读模式打开文件。

# 基本的写入文件
with open("files/write_file.txt", "a") as write_file:
    str_en = "hello Python"
    write_file.write(str_en + "\n")


username = input("input your name please:")
username_file = codecs.open("files/username.txt","w","utf-8")
if username != '':
    username_file.write(username+"\n")

print("your name were record in my system")