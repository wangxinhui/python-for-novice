# 使用用户输入来填充字典
responses = {}
active = True
while active:
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")
    responses[name.rstrip()] = response.rstrip()

    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat=='no':
        active = False

print("\n--- Poll Results ---")
for name, response in responses.items():
    print(name + " would like to climb " + response + ".")