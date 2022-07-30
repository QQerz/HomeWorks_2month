from cars.create_car import Car
from cars.get_car_info import get_car_info

bmw = Car('BMW', 'M8', 'Black', 'm490')

print(get_car_info('BMW', 'M8', 'Black', 'm490'))

print(Car.start_engine())
print(Car.stop_engine())