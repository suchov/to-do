# just an example of a class and inheritance from a class
class Vehicle:
    def __init__(self, max_speed, efficiency):
        self.max_speed = max_speed
        self.efficiency = efficiency

    def get_trip_cost(self, distance, fuel_price):
        return (distance / self.efficiency) * fuel_price

    def get_cargo_volume(self):
        pass


class Truck(Vehicle):
    def __init__(
        self,
        max_speed,
        efficiency,
        load_weight,
        bed_area,
    ):
        Vehicle.__init__(self, max_speed, efficiency)
        self.load_weight = load_weight
        self.bed_area = bed_area

    def get_trip_cost(self, distance, fuel_price):
        return Vehicle.get_trip_cost(self, distance, fuel_price) + self.load_weight * 0.01

    def get_cargo_volume(self):
        return self.bed_area * 2


class Car(Vehicle):
    def __init__(self, max_speed, efficiency, cargo_volume):
        Vehicle.__init__(self, max_speed, efficiency)
        self.cargo_volume = cargo_volume

    def get_cargo_volume(self):
        return self.cargo_volume
