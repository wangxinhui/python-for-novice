# 将函数存储在模块中
# import pizza
# pizza.make_pizza('21',"辣椒","白糖","生姜","盐","醋")

# 导入指定的方法
from pizza import print_1
print_1()

# 使用as 给函数指定别名
from pizza import print_2 as p2
p2()

# 使用as 给模块指定别名
import pizza as piz
piz.make_pizza('21',"辣椒","白糖")