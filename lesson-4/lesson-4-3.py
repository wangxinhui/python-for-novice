# 创建数值列表
# 使用函数range()
for value in range(0,5):
    print(value)

# 使用range() 创建数字列表
numbers = list(range(1,6))
print(numbers)

# range函数指定步长 range(2,11,2) 从2-11，步长是2
even_numbers = list(range(2,11,3))
print(even_numbers)

squares =[]
for value in range(1,11):
    squares.append(value**2)

print(squares)
# 获取列表最小值
print(min(squares))
# 获取列表最大值
print(max(squares))
# 求和
print(sum(squares))

# 列表解析
# 要使用这种语法，首先指定一个描述性的列表名，如squares ；
# 然后，指定一个左方括号，并定义一个表达式，用于生成你要存储到列表中的值。在这个示例中，表达
# 式为value**2 ，它计算平方值。
# 接下来，编写一个for 循环，用于给表达式提供值，再加上右方括号。
# 在这个示例中，for 循环为for value in range(1,11) ，它将值1~10提供给表达式value**2 。
# 请注意，这里的for 语句末尾没有冒号。
squares_1 = [value**4 for value in range(1,11)]
print(squares_1)


