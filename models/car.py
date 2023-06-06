"""
This is file with car model.
"""
from .transport import Transport
from decorators import logged
from exceptions import SpeedExceededException


# pylint: disable=line-too-long
# pylint: disable=too-many-arguments
class Car(Transport):
    """
    A class representing a car.

    Attributes:
        door_count (int): number of doors in the car.
        trunk_volume (float): volume of the trunk in liters.
        max_load (float): maximum load capacity of the car in kilograms.

    Methods:
        accelerate(self, speed): Accelerates the car to the specified speed.

    Properties:
        door_count: Get or set the number of doors in the car.
        trunk_volume: Get or set the volume of the trunk in liters.
        max_load: Get or set the maximum load capacity of the car in kilograms.
    """

    def __init__(self, transport_id, max_speed, door_count, trunk_volume, max_load):
        """
        Initialize a Car object with the provided parameters.

        Args:
            id (int): The unique identifier for the car.
            max_speed (float): The maximum speed of the car.
            door_count (int): The number of doors on the car.
            trunk_volume (float): The volume of the car's trunk in cubic units.
            max_load (float): The maximum load capacity of the car in weight units.

        Returns:
            None
        """

        super().__init__(transport_id, max_speed)
        self.door_count = door_count
        self.trunk_volume = trunk_volume
        self.max_load = max_load

    def __str__(self):
        """
            Return a string representation of the Car object.

            Returns:
                str: A string representing the Car object with its attributes.

        """
        return f"Car(id={self.transport_id}, max_speed={self.max_speed}, door_count={self.door_count}, " \
               f"trunk_volume={self.trunk_volume}, max_load={self.max_load})"

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
