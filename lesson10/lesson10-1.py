# with open('pi_digits.txt') as file_object:
#     contents = file_object.read()
#     print(contents.rstrip())

# 逐行读取
with open('files/pidigits.txt') as file_object:
    print(file_object.read())
    # for line in file_object:
    #     print(line.rstrip())


with open("files/pidigits.txt") as file_object1:
    lines = file_object1.readlines()

for line in lines:
    print(line.rstrip())

# 使用文件的内容
with open("files/pidigits.txt") as file_object2:
    lines = file_object2.readlines()
str1 = '';
for line in lines:
    str1 += line.strip()
print(str1[:52]+ '......')
print(len(str1[:52]))
print(len(str1))
# 判断你的生日是否出现在圆周率中
with open("files/pidigits.txt") as file_object3:
    lines = file_object3.readlines()
str2 = '';
for line in lines:
    str2 += line.strip()
birthday = input("input your birthday :")
if birthday in str2:
    print("your birthday is in pi")
else:
    print("not in")