# 列表

# 在Python中，用方括号（[] ）来表示列表，并用逗号来分隔其中的元素。下面是一个简单的列表示例，这个列表包含几种自行车：
bicycles = ['trek',"cannondale",'redline',"specialized",1]
print(bicycles)   # result is ['trek', 'cannondale', 'redline', 'specialized']

print(bicycles[0])  # 列表是有序集合，索引从0开始

print(bicycles[0].title())

print(str(bicycles[4]).title())

# Python为访问最后一个列表元素提供了一种特殊语法。通过将索引指定为-1 ，可让Python返回最后
# 一个列表元素   -2 -3 -4 返回倒数 2，3，4个元素
print(bicycles[-1])
print(bicycles[-2])

# 修改，添加和删除元素
motorcycles = ['honda','yamaha','suzuki']

# 修改
motorcycles[0] = 'ofo'
print(motorcycles)
# 添加
motorcycles.append('mobo')
print(motorcycles)
# 插入
motorcycles.insert(0,'小黄车')
print(motorcycles)

# 删除
del motorcycles[2]
print(motorcycles)

# 使用方法 pop() 删除元素 弹出最后一个元素
popped_motorcycles = motorcycles.pop()
# 最后一个元素
print(popped_motorcycles)
# 剩下的元素
print(motorcycles)
# 弹出指定元素
popped_index = motorcycles.pop(1)
print(popped_index)
print(motorcycles)
# 根据元素的值来删除元素
motorcycles.remove('suzuki')
print(motorcycles)
