from .transport import Transport


class Car(Transport):
    """
    A class representing a car.

    Attributes:
        __door_count (int): number of doors in the car.
        __trunk_volume (float): volume of the trunk in liters.
        __max_load (float): maximum load capacity of the car in kilograms.

    Methods:
        accelerate(self, speed): Accelerates the car to the specified speed.

    Properties:
        door_count: Get or set the number of doors in the car.
        trunk_volume: Get or set the volume of the trunk in liters.
        max_load: Get or set the maximum load capacity of the car in kilograms.
    """

    def __init__(self, id, max_speed, door_count, trunk_volume, max_load):
        super().__init__(id, max_speed)
        self.__door_count = door_count
        self.__trunk_volume = trunk_volume
        self.__max_load = max_load

    @property
    def door_count(self):
        return self.__door_count

    @door_count.setter
    def door_count(self, value):
        self.__door_count = value

    @property
    def trunk_volume(self):
        return self.__trunk_volume

    @trunk_volume.setter
    def trunk_volume(self, value):
        self.__trunk_volume = value

    @property
    def max_load(self):
        return self.__max_load

    @max_load.setter
    def max_load(self, value):
        self.__max_load = value

    def __str__(self):
        return f"Car(id={self.id}, max_speed={self.max_speed}, door_count={self.__door_count}, " \
               f"trunk_volume={self.__trunk_volume}, max_load={self.__max_load})"

    def accelerate(self, speed):
        return speed
