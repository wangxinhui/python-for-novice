# 嵌套 字典嵌套列表
pizza = {'crust': 'thick', 'toppings': ['mamamma','wawawawawaaw']}
print("you ordered a " + pizza['crust'] +"-crust pizza.")
for top in pizza['toppings']:
    print("\t" + top)

# 在字典中存储字典
users = {
    'wang': {'a': 'aaa', 'b': 'bbb', 'c': 'ccc'},
    'xin': {'aa':'aaaa','bb': 'bbbb', 'cc': 'cccc'}
}
for name,user_info in users.items():
    print("Username:" + name)
    for key,value in user_info.items():
        print("\nfull name" + key + " " + value)
    print()