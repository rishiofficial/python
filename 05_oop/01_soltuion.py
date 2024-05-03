class Car:

    def __init__(self,model,brand):
        self.model = model
        self.brand = brand

    def __get_brand(self):
        return f'{self.brand} !'
    
    def fuel_type(self):
        return "petrol or diesel"
    
    def full_name(self):
        return f"{self.model} {self.brand}"
    @staticmethod
    def general_description():
        return "Cars are means of transport and have comfort "
    
class ElectricCar(Car):
    def __init__(self, model, brand,batery_size):
        self.batery_size = batery_size
        super().__init__(model, brand)

    def fuel_type(self):
        return "Electric charge"
    
   


# my_tesla = ElectricCar('Tesla','Model s','85kwh')
# print(my_tesla.full_name())
# my_car = Car("Toyota", "Corola")

# print(my_tesla.fuel_type())
# print(my_car.general_description())
# print(Car.general_description())
# print(my_car.brand)
# print(my_car.model)
# print(my_car.full_name())


class Engine:
    def engine_info(self):
        return "This is engine"
    
class Battery:
    def battery_info(self):
        return "This is battery"
    
class ElectriccarTwo(Engine,Battery, Car):
    pass
my_new_teslacar = ElectriccarTwo('tesla','20')
print(my_new_teslacar.battery_info())
print(my_new_teslacar.engine_info())
