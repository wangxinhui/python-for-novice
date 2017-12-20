# 使用列表的一部分 - 切片
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])  # ['charles', 'martina', 'michael']
print(players[:4])   # 没指定开头，从0开始['charles', 'martina', 'michael', 'florence']
print(players[2:])   # 没指定结束，从n开始到结束 ['michael', 'florence', 'eli']
# 可以使用负数，来获取最后几个元素
print(players[-2:])  # ['florence', 'eli']
print(players[:-2])  # ['charles', 'martina', 'michael']

# 遍历切片
for play in players[:3]:
    print(play.title())

# 复制列表
my_foods = ['pizza', 'falafel', 'carrot cake']
# friend_foods = my_foods
# my_foods.append('ice')
# friend_foods.append('chooleate')
# print(my_foods)
# print(friend_foods)
# 上面的复制，我试了一下，他们两个最后的值都是一样的，应该是指向了同一个地址，所以是错误的

# 下面是正确的复制列表的方式
friend_foods = my_foods[:]
my_foods.append('ice')
friend_foods.append('chocolate')
print(my_foods)
print(friend_foods)