"""
This is file with tram model.
"""
from .transport import Transport
from decorators import logged
from exceptions import SpeedExceededException


class Tram(Transport):
    """
    A class representing a tram.

    Attributes:
        route_number (int): Number of the tram's route.
        capacity (int): Capacity of the tram.

    Properties:
        route_number (int): Number of the tram's route.
        capacity (int): Capacity of the tram.

    Methods:
        accelerate(self, speed): Accelerates the tram to the specified speed.

    """

    def __init__(self, transport_id, max_speed, route_number, capacity):
        """
        Initialize a Bus object with the provided parameters.

        Args:
            transport_id (int): The unique identifier for the bus.
            max_speed (float): The maximum speed of the bus.
            route_number (int): The number associated with the bus route.
            capacity (int): The maximum number of passengers the bus can hold.

        Returns:
            None
        """
        super().__init__(transport_id, max_speed)
        self.route_number = route_number
        self.capacity = capacity

    @logged(SpeedExceededException, "file")
    def accelerate(self, speed):
        """
        Accelerates the trolleybus to the specified speed.

        Args:
            speed (int): The speed to which the trolleybus will be accelerated.

        Returns:
            int: The actual speed the trolleybus has been accelerated to.

        """
        if speed > self.max_speed:
            raise SpeedExceededException()

        return speed

    def __str__(self):
        """
            Return a string representation of the Tram object.

            Returns:
                str: A string representing the Tram object with its attributes.

            """
        return f"Tram(id={self.transport_id}, max_speed={self.max_speed}, " \
               f"route_number={self.route_number}, capacity={self.capacity})"
