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
