# 异常--------------------
# print(4.4/0.0)
# try:
#     print(4/0)
# except ZeroDivisionError:
#     print("your can't divide by zero")
# 异常----------------------

# try except else模式 ----------------------------------
# print("Give me two numbers, and I'll divide them.")
# print("Enter 'q' to quit.")
# while True:
#     first_number = input("First Number:")
#     if first_number =='q':
#         break
#     second_number = input("Second Number:")
#     try:
#         answer = int(first_number) / int(second_number)
#     except ZeroDivisionError:
#         print("your can't divide by zero")
#     else:
#         print(answer)
# try except else模式 ----------------------------------

# 读取不存在的文件------------------------------------------
# filename = 'files/alice.txt'
# try:
#     with open(filename) as f_obj:
#         contents = f_obj.read()
# except FileNotFoundError:
#     print(filename + " file not found")
# else:
#     print(contents)
# 读取不存在的文件------------------------------------------

# 分析文本-------------------------------------------------
# filename = 'files/alice.txt'
# try:
#     with open(filename) as f_obj:
#         contents = f_obj.read()
# except FileNotFoundError:
#     print(filename + " file not found")
# else:
#     words = contents.split()
#     print(len(words))

# 使用多个文件


def get_count(filename):
    try:
        with open(filename,encoding='utf-8') as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        # 失败时一声不吭
        pass
        # 失败时给出提示
        # print(filename + " file not found")
    else:
        words = contents.split()
        print(len(words))

filenames = ["files/alice.txt","files/pidigits.txt","files/aaaa.txt"]
for filename in filenames:
    get_count(filename)