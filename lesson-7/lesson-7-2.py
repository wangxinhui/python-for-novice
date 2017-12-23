# while循环
# current_number = 1
# while current_number <= 5:
#     print(current_number)
#     current_number += 1

# prompt = "\nTell me something, and I will repeat it back to you:"
# prompt += "\nEnter 'quit' to end the program. "
# message = ""
# while message!='quit':
#     message=input(prompt)
#     if message!='quit':
#         print(message)

# 标志
# prompt = "\nTell me something, and I will repeat it back to you:"
# prompt += "\nEnter 'quit' to end the program. "
# active = True
# while active:
#     message = input(prompt)
#     if message == 'quit':
#         active = False
#     else:
#         print(">>>>>>>>>>" + message)

# 使用 break 退出循环
# 要立即退出 while 循环,不再运行循环中余下的代码,也不管条件测试的结果如何,可使用 break 语句。
# prompt = "\nTell me something, and I will repeat it back to you:"
# prompt += "\nEnter 'quit' to end the program. "
#
# while True:
#     message = input(prompt)
#     if message == 'quit':
#         break
#     else:
#         print(">>>>>>>>>>" + message)

# 在循环中使用 continue
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number%2==0:
        continue
    else:
        print(current_number)

# 删除包含特定值的所有列表元素
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')

print(pets)