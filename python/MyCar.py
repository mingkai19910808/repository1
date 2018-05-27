#导入类
from Class import Car,ElectricCar
my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 23
my_new_car.read_odometer()

my_tesla = ElectricCar('tesla', 'model s', 2016,10)
print(my_tesla.get_descriptive_name())
my_tesla.increment_odometer2(10)
my_tesla.battery.describe_battery()


#导入整个模块
import Class
my_beetle = Class.Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())
my_tesla = Class.ElectricCar('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive_name())