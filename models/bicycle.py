from .transport import Transport


class Bicycle(Transport):
    """
    A class representing a bicycle.

    Attributes:
        __bike_brand (str): Brand of the bicycle.

    Properties:
        bike_brand (str): Brand of the bicycle.

    Methods:
        accelerate(self, speed): Accelerates the bicycle to the specified speed.
    """
    def __init__(self, id, max_speed, bike_brand):
        super().__init__(id, max_speed)
        self.__bike_brand = bike_brand

    @property
    def bike_brand(self):
        return self.__bike_brand

    @bike_brand.setter
    def bike_brand(self, value):
        self.__bike_brand = value

    def accelerate(self, speed):
        return speed

    def __str__(self):
        return f"Bicycle(id={self.id}, max_speed={self.max_speed}, bike_brand={self.__bike_brand}"
