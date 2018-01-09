from Car import Car as carrrr

class Dog():
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.title() + " is siting now.")
    def roll_over(self):
        print(self.name.title() + " rolled over.")





my_car = carrrr("adf","132","123")
print(my_car.get_descriptive_name())

# 创建实例
# my_dog = Dog('Willie',6)
# print("My dog's name is " + my_dog.name + ".")
# print("My dog is " + str(my_dog.age) + " years old.")
# my_dog.sit()
# my_dog.roll_over()