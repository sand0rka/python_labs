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
        self.transports.append(transport)

    def find_transport_with_max_speed_higher_than(self, max_speed):
        return [transport for transport in self.transports if transport.max_speed > max_speed]

    def find_transport_by_id(self, id):
        return [transport for transport in self.transports if transport.id == id]
