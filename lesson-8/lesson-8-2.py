# 让实参变成可选的
def get_formatted_name(first_name, middle_name, last_name):
    full_name = first_name + ' ' + middle_name + ' ' + last_name
    return full_name.title()

name = get_formatted_name("Xin","Hui","Wang")
print(name)

def get_formatted_name(first_name, last_name, middle_name=''):
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name

    return full_name

f_name = get_formatted_name("XinHui","Wang","liu")
print(f_name)

# 返回字典
def build_person(first_name,last_name,age=''):
    person =  {'firstName':first_name, 'lastName':last_name}
    if int(age)>12:
        person['age'] = age
    return person

name = build_person('Xinhui','Wang','13')
print(name)

# 传递列表
def greet_users(users):
    for name in users:
        print("Hello: " + name)

users = ['小猫','小狗','小猪']
greet_users(users)