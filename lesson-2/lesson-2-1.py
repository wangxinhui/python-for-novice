# 变量的命名和使用
# 变量名只能包含字母、数字和下划线。变量名可以字母或下划线打头，但不能以数字打头，例如，可将变量命名为message_1，但不能将其命名为1_message。

message = 'Hello python world!'
print(message)

message = 'Hello Python Crash Course world!'
print(message)

# 字符串
# 用引号括起的都是字符串,其中的引号可以是单引号,也可以是双引号
"this is a String"
'this is  also a String'
'I told my friend, "Python is my favorite language!"'
"The language 'Python' is named after Monty Python, not the snake."
"One of Python's strengths is its diverse and supportive community."

# 使用方法修改字符串的大小写(首字母大写)
name = "ada lovelace"
print(name.title())
print(name.upper())
print(name.lower())

# 合并(拼接)字符串
first_name = "xinhui"
last_name = "wang"
full_name = first_name + " " + last_name
print(full_name)

# 使用制表符或换行符来添加空白
print("\tPython")
print("\n\tPython")
# 删除空白 rstrip(右) lstrip（左） strip（两边）
favorite_language = 'python '
print(favorite_language.rstrip())
print(favorite_language)

