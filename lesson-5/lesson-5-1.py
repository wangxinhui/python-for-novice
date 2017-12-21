# if 语句
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car=='bmw':
        print(car.upper())
    else:
        print(car.title())
print("the for is over")

# 检查是否不相等
requested = 'mushrooms'
if requested != 'anchovies':
    print("Hold the anchovies")

# 比较数字
age = 18
print(age==18)
if age != 18:
    print("age not equals 18")
else:
    print("age equals 18")

# 检查多个条件 and
age_0 = 22
age_1 = 18
if (age_0 >= 21) and (age_1 >= 21):
    print("age_0 and age_1 all >= 21")
else:
    print("age_0 and age_1 not all >= 21")

# 检查多个条件 or
if (age_0 >= 21) or (age_1 >= 21):
    print("age_0 or age_1 is >= 21")
else:
    print("age_0 or age_1 is >= 21")

# 检查特定值是否包含在列表中 in  , not in
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user in banned_users:
    print(" he is in banned_users")
if user not in banned_users:
    print("he is not in banned_users")

# 布尔表达式
game_active = True
can_edit = False
