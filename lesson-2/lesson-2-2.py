# 数字 + - * /  **(平方)
print(2+3)
print(1+7)
print(16/2)
print(9-1)
print(2**3)
print(2*4)
#  Python 2 中的整数 是1 3.0 /2
print(3/2)
# 浮点型
print(0.2 + 0.1) #结果是0.30000000000000004 暂时忽略多余的小数位数即可;后面的学习在需要时处理多余小数位的方式。

#使用函数str()避免类型错误 请不要
age =23
message_error = "Happy " + age + "rd Birthday" # TypeError: age must be str, not int
message = "Happy " + str(age) + "rd Birthday"

print(message)