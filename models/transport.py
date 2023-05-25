"""
This is file with transport model.
"""
from abc import ABC, abstractmethod

# pylint: disable=too-few-public-methods
class Transport(ABC):
    """
        Abstract base class representing a transport vehicle.

        Attributes:
            transport_id (int): Unique identifier of the transport vehicle. Default value is 0.
            max_speed (float): Maximum speed of the transport vehicle.

        Methods:
            accelerate(speed): Abstract method to accelerate the transport vehicle.

        Properties:
            id (int): Unique identifier of the transport vehicle. Default value is 0.
            max_speed (float): Maximum speed of the transport vehicle.
    """

    def __init__(self, transport_id=0, max_speed=0):
        """
        Initialize a Vehicle object with the provided parameters.

        Args:
            transport_id (int): The unique identifier for the vehicle. Defaults to 0.
            max_speed (float): The maximum speed of the vehicle. Defaults to 0.0.

        Returns:
            None
        """
        self.transport_id = transport_id
        self.max_speed = max_speed

    @abstractmethod
    def accelerate(self, speed):
        """
            Abstract method to accelerate the transport vehicle.

            Args:
                speed (float): Speed to which the transport vehicle should be accelerated.
        """
