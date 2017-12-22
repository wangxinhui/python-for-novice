# 遍历字典
user_0 = {
    'username': 'efemi',
    'first': 'entico',
    'last': 'efemi',
}
for key,value in user_0.items():
    print("\nkey: " + key)
    print("value:" + value)


favorite_languages = {
    'jen': 'python',
    'Wang Xin Hui': 'java',
    'lily': 'C',
    'lucy': 'python'
}
friends = ['lucy', 'lily']
for name in favorite_languages.keys():
    print(name.title())
    if name in friends:
        print("Hi " + name.title()
              + ",I see your favorite language is " + favorite_languages[name].title() + ".")

if 'erin' not in favorite_languages.keys():
    print("Erin,please take our poll !")

# 按顺序遍历字典中的所有键
for name in reversed(sorted(favorite_languages.keys())):
    print(name.title() + " thank you for taking the poll.")

for name in favorite_languages.values():
    print(name.title() + " thank you for taking the poll.")
