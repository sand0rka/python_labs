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
            fuel_set (set): Set storing the fuel data for the transport vehicle.

        Methods:
            accelerate(speed): Abstract method to accelerate the transport vehicle.
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
        self.fuel_set = set()

    @abstractmethod
    def accelerate(self, speed):
        """
            Abstract method to accelerate the transport vehicle.

            Args:
                speed (float): Speed to which the transport vehicle should be accelerated.
        """

    def __iter__(self):
        """
        Returns an iterator over the fuel_set of the transport vehicle.

        Returns:
            iterator: Iterator over the fuel_set.
        """
        return iter(self.fuel_set)

    def get_attributes_by_type(self, data_type):
        """
        Get a dictionary of attributes and their values based on the specified data type.

        Args:
            data_type (type): The data type of the attribute values to filter.

        Returns:
            dict: A dictionary containing attribute names as keys and their corresponding values.
                  Only attributes with values of the specified data type are included.
        """
        return {key: value for key, value in self.__dict__.items() if isinstance(value, data_type)}
