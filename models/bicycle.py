"""
This is file with bicycle model.
"""
from .transport import Transport

# pylint: disable=line-too-long
class Bicycle(Transport):
    """
    A class representing a bicycle.

    Attributes:
        bike_brand (str): Brand of the bicycle.

    Properties:
        bike_brand (str): Brand of the bicycle.

    Methods:
        accelerate(self, speed): Accelerates the bicycle to the specified speed.
    """

    def __init__(self, transport_id, max_speed, bike_brand):
        """
        Initialize a Bicycle object with the provided parameters.

        Args:
            id (int): The unique identifier for the bicycle.
            max_speed (float): The maximum speed of the bicycle.
            bike_brand (str): The brand of the bicycle.

        Returns:
            None
        """
        super().__init__(transport_id, max_speed)
        self.bike_brand = bike_brand

    def accelerate(self, speed):
        """Accelerates the trolleybus to the specified speed.

            Args:
                speed (int): The speed to which the trolleybus will be accelerated.

            Returns:
                int: The actual speed the trolleybus has been accelerated to.

        """
        return speed

    def __str__(self):
        """
        Return a string representation of the Bicycle object.

        Returns:
            str: A string representing the Bicycle object with its attributes.
        """
        return f"Bicycle(id={self.transport_id}, max_speed={self.max_speed}, bike_brand={self.bike_brand}"
