class ParkingSystem:
    places = dict()

    def __init__(self, big: int, medium: int, small: int):
        self.places[1] = big
        self.places[2] = medium
        self.places[3] = small

    def addCar(self, carType: int) -> bool:
        if self.places[carType] > 0:
            self.places[carType] -= 1
            return True
        else:
            return False

# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)