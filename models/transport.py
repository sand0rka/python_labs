from abc import ABC, abstractmethod


class Transport(ABC):
    """
        Abstract base class representing a transport vehicle.

        Attributes:
            id (int): Unique identifier of the transport vehicle. Default value is 0.
            max_speed (float): Maximum speed of the transport vehicle.

        Methods:
            accelerate(speed): Abstract method to accelerate the transport vehicle.

        Properties:
            id (int): Unique identifier of the transport vehicle. Default value is 0.
            max_speed (float): Maximum speed of the transport vehicle.
    """
    @abstractmethod
    def __init__(self, id=0, max_speed=0):
        self.id = id
        self.max_speed = max_speed

    @abstractmethod
    def accelerate(self, speed):
        """
            Abstract method to accelerate the transport vehicle.

            Args:
                speed (float): Speed to which the transport vehicle should be accelerated.
        """
        pass
