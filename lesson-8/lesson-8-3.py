def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop();
        print("Printing model: " + current_design)
        completed_models.append(current_design);

def show_completed_models(completed_models):
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
# 禁止函数修改列表
# print_models(unprinted_designs[:],completed_models)  # 传递一个副本
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)
print(unprinted_designs)

# 传递任意数量的实参
def make_pizza(*toppings):
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)

make_pizza('123','456','789')

# 使用任意数量的关键字实参
def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key,value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('albert', 'einstein',
location='princeton',
field='physics')
print(user_profile)