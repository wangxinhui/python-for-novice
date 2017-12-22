# 字典
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

print(alien_0['color'])
print(alien_0['points'])

# 添加键 — 值对
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# 创建一个空字典
alien_1 = {}
alien_1['color'] = 'red'
print(alien_1)
# 修改字典中的值
alien_1['color'] = 'orange'
print(alien_1)
# 删除键值对
# 注意:删除的键—值对永远消失了
del alien_0['color']
print(alien_0)

favorite_languages = {
    'jen': 'python',
    'Wang Xin Hui': 'java',
    'lily': 'C',
    'lcuy': 'python'
}

print("Wang Xin Hui favorite language is :"
      + favorite_languages['Wang Xin Hui'] + '.')