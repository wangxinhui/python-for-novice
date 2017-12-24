# 函数
def great_user():
    # 文档字符串(docstring)的注释, 描述了函数是做什么的。文档字符串用三引号括起, Python使用它们来生成有关程序中函数的文档。
    """显示简单的问候语"""
    print("Hello")
great_user()

# 向函数传递信息
def great_user_1(user_name):
    print(user_name.title() +">>>>>>>>>>>")

great_user_1('haha')

# 实参和形参
def great_user_2(user_name):
    print(user_name.title() + "<><><><><><><><>")
great_user_2('wangxinhui')

# 默认值
def describe_pet(pet_name,animal_type='dog',color='green'):
    print("\nI have a "+ color.title() + " " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

def describe_pet(pet_name,animal_type='dog'):
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
describe_pet('单身猫',"cat")

# 返回值
def getUserName(singleDog):
    return "Hello " + singleDog.title()

name = getUserName('你是单身狗')
print(name)