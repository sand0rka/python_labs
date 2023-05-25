"""
This is file with transport manager.
"""

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

    """
    transports = []

    def add_transport(self, transport):
        """
        Add a transport object to the list of transports.

        Args:
            transport: The transport object to be added.

        Returns:
            None
        """
        self.transports.append(transport)

    def find_transport_with_max_speed_higher_than(self, max_speed):
        """
        Find transports with a maximum speed higher than the specified value.

        Args:
            max_speed (float): The maximum speed threshold to compare with.

        Returns:
            list: A list of transports with a maximum speed higher than max_speed.
        """
        return [transport for transport in self.transports if transport.max_speed > max_speed]

    def find_transport_by_id(self, transport_id):
        """
        Find a transport object by its ID.

        Args:
            transport_id: The unique identifier of the transport object.

        Returns:
            list: A list of transport objects with a matching ID. If no transport is found, the list will be empty.
        """
        return [transport for transport in self.transports if transport.transport_id == transport_id]
