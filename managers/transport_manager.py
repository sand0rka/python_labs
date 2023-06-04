"""
This is file with transport manager.
"""
from decorators import print_iterable_length, logged
from exceptions import TransportNotFoundException


# pylint: disable=line-too-long
class TransportManager:
    """
    A class that manages a collection of transports.

    Attributes:
        transports (list): A list of transports.

    Methods:
        add_transport(transport): Add transport to the collection.
        find_transport_with_max_speed_higher_than(max_speed): Find transports with max speed higher than given value.
        find_transport_by_id(id): Find transport with a specific ID.
        get_list_of_accelerate(): Get a list of accelerate values for each transport.
        get_enumerate(): Get an enumeration of the transports.
        get_zip(): Get a zip of transports with their corresponding to accelerate values.
        find_transport_by_max_speed(speed): Check if any or all transports have a certain max speed.
    """
    transports = []

    def __init__(self):
        """
        Initializes a set_manager object.

        """
        self._current_index = 0

    def __len__(self):
        """
        Get the number of transports in the transport manager.

        Returns:
            int: The number of transports.
        """
        return len(self.transports)

    def __getitem__(self, index):
        """
        Get a transport object by index.

        Args:
            index (int): The index of the transport object.

        Returns:
            object: The transport object at the specified index.
        """
        return self.transports[index]

    def __iter__(self):
        """
        Iterate over the transports in the transport manager.

        Returns:
            iterator: Iterator over the transports.
        """
        return self

    def __next__(self):
        """
        Get the next transport object in the iteration.

        Returns:
            object: The next transport object.

        Raises:
            StopIteration: If there are no more transports to iterate over.
        """
        if self._current_index >= len(self.transports):
            raise StopIteration
        else:
            transport = self.transports[self._current_index]
            self._current_index += 1
            return transport

    def add_transport(self, transport):
        """
        Add a transport object to the list of transports.
        Args:
            transport: The transport object to be added.
        Returns:
            None
        """
        self.transports.append(transport)

    @print_iterable_length
    def find_transport_with_max_speed_higher_than(self, max_speed):
        """
        Find transports with a maximum speed higher than the specified value.

        Args:
            max_speed (float): The maximum speed threshold to compare with.

        Returns:
            list: A list of transports with a maximum speed higher than max_speed.
        """
        return [transport for transport in self.transports if transport.max_speed > max_speed]

    @logged(TransportNotFoundException, "console")
    def find_transport_by_id(self, transport_id):
        """
        Find a transport object by its ID.

        Args:
            transport_id: The unique identifier of the transport object.

        Returns:
            list: A list of transport objects with a matching ID. If no transport is found, the list will be empty.
        """
        matching_transports = [transport for transport in self.transports if transport.transport_id == transport_id]

        if not matching_transports:
            raise TransportNotFoundException

        return matching_transports

    def get_list_of_accelerate(self):
        """
        Get a list of accelerate values for each transport.

        Returns:
            list: A list of accelerate values.
        """
        return [transport.accelerate() for transport in self.transports]

    def get_enumerate(self):
        """
        Get an enumeration of the transports.

        Returns:
            enumerate: An enumeration of the transports.
        """
        return enumerate(self.transports)

    def get_zip(self):
        """
        Get a zip of transports with their corresponding to accelerate values.

        Returns:
            zip: A zip of transports and their accelerate values.
        """
        return zip(self.transports, self.get_list_of_accelerate())

    def find_transport_by_max_speed(self, speed):
        """
        Check if any or all transports have a certain max speed.

        Args:
            speed: The max speed to check.

        Returns:
            dict: A dictionary indicating if all or any transports have the specified max speed.
        """
        return {"all": all(transport.max_speed == speed for transport in self.transports),
                "any": any(transport.max_speed == speed for transport in self.transports)}
