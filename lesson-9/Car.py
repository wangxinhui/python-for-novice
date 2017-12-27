class Car():
    # _init__()是一个特殊的方法, 每当你根据Dog类创建新实例时, Python都会自动运行它。
    # 在这个方法的名称中, 开头和末尾各有两个下划线, 这是一种约定, 旨在避免Python
    # 默认方法与普通方法发生名称冲突。
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        # 给属性指定默认值
        self.odometer = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer) + " miles on it.")

    def update_odometer(self, mileage):
        self.odometer = mileage

    # 通过方法对属性的值进行递增
    def increment_odometer(self, miles):
        self.odometer += miles


my_new_car = Car('Audi', 'a4', '2016')
myname = my_new_car.get_descriptive_name()
my_new_car.read_odometer()
print(myname)
# 直接修改属性的值
my_new_car.odometer = 10000
my_new_car.read_odometer()
# 通过方法修改属性的值
my_new_car.update_odometer(20)
my_new_car.read_odometer()
# 通过方法对属性的值进行递增
my_new_car.increment_odometer(100)
my_new_car.read_odometer()


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = 70

    def describe_battery(self):
        print("This car has a " + str(self.battery_size) + "-Km battery .")


my_ele_car = ElectricCar('dazhou', 'models', '2017')
print(my_ele_car.get_descriptive_name())
my_ele_car.describe_battery()
