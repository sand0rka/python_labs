from .Transport import Transport


class Tram(Transport):
    """
    A class representing a tram.

    Attributes:
        __route_number (int): Number of the tram's route.
        __capacity (int): Capacity of the tram.

    Properties:
        route_number (int): Number of the tram's route.
        capacity (int): Capacity of the tram.

    Methods:
        accelerate(self, speed): Accelerates the tram to the specified speed.

    """

    def __init__(self, id, max_speed, route_number, capacity):
        super().__init__(id, max_speed)
        self.__route_number = route_number
        self.__capacity = capacity

    @property
    def route_number(self):
        return self.__route_number

    @route_number.setter
    def route_number(self, value):
        self.__route_number = value

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        self.__capacity = value

    def accelerate(self, speed):
        return speed

    def __str__(self):
        return f"Tram(id={self.id}, max_speed={self.max_speed}, "\
                f"route_number={self.__route_number}, capacity={self.__capacity})"
