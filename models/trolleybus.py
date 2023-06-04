"""
This is file with trolleybus model.
"""
from .transport import Transport

# pylint: disable=line-too-long
# pylint: disable=too-many-arguments
class Trolleybus(Transport):
    """
    A class representing a trolleybus.

    Attributes:
        transport_id (int): unique identifier of the trolleybus, the default value is 100;
        route_number (int): number of the route on which the trolley runs;
        current_stop (String): the current stop at which the trolleybus is located;
        max_speed (float): the maximum speed of the trolleybus;
        capacity (int): the capacity of the trolleybus (the number of passengers that the trolleybus can carry);
        passengers (int): the current number of passengers carried by the trolleybus.

    Methods:
        stop(self): stops the trolley at the current stop (changes the speed to 0);
        start(self): sets the current speed of the trolleybus to 20 km/h;
        add_passenger(self): adds one passenger to the trolleybus (if there are enough free seats);
        remove_passenger(self): removes one passenger from the trolley (if there is one in the trolley);
        __str__(self): returns a string representation of the Trolleybus object.

    Properties:
        id: unique identifier of the trolleybus, the default value is 100;
        route_number: number of the route on which the trolley runs;
        current_stop: the current stop at which the trolleybus is located;
        max_speed: the maximum speed of the trolleybus;
        capacity: the capacity of the trolleybus (the number of passengers that the trolleybus can carry);
        passengers: the current number of passengers carried by the trolleybus.
    """

    default_trolleybus = None

    def __init__(self, transport_id=100, max_speed=0.0, route_number=0, current_stop="", capacity=0, passengers=0):
        """
        Initialize a Bus object with the provided parameters.

        Args:
            id (int): The unique identifier for the bus. Defaults to 100.
            max_speed (float): The maximum speed of the bus. Defaults to 0.0.
            route_number (int): The number associated with the bus route.
            current_stop (str): The name of the current bus stop.
            capacity (int): The maximum number of passengers the bus can hold.
            passengers (int): The current number of passengers on the bus.

        Returns:
            None
        """
        super().__init__(transport_id, max_speed)
        self.route_number = route_number
        self.current_stop = current_stop
        self.max_speed = max_speed
        self.capacity = capacity
        self.passengers = passengers

    def __cmp__(self, other):
        """
        Compare 2 objects.

        Returns:
            bool
        """
        return self.route_number == other.route_number and self.current_stop == other.current_stop and \
                self.max_speed == other.max_speed and self.capacity == other.capacity and \
                self.passengers == other.passengers

    def stop(self):
        """
        Stops the vehicle by setting the acceleration to 0.
        """
        self.accelerate(0)

    def start(self):
        """
        Starts the vehicle by accelerating to a speed of 20.
        """
        self.accelerate(20)

    def add_passenger(self):
        """
        Adds a passenger to the vehicle, if there is available capacity.
        """
        if self.passengers < self.capacity:
            self.passengers += 1

    def remove_passenger(self):
        """
        Removes a passenger from the vehicle, if there is any.
        """
        if self.passengers > 0:
            self.passengers -= 1

    def __str__(self):
        """
        Write string for trolleybus.
        """
        return f"Trolleybus(id={self.transport_id}, max_speed={self.max_speed}, route_number={self.route_number}, " \
               f"current_stop='{self.current_stop}', capacity={self.capacity}, passengers={self.passengers})"

    @staticmethod
    def get_instance():
        """
        Returns the default instance of the Trolleybus class.

            If the default instance does not exist, a new instance of Trolleybus will be created
            and set as the default instance. Subsequent calls to this method will return the same
            default instance.

        Returns:
            Trolleybus: The default instance of the Trolleybus class.

        """
        if Trolleybus.default_trolleybus is None:
            Trolleybus.default_trolleybus = Trolleybus()
        return Trolleybus.default_trolleybus

    def accelerate(self, speed):
        """
        Accelerates the trolleybus to the specified speed.

        Args:
            speed (int): The speed to which the trolleybus will be accelerated.

        Returns:
            int: The actual speed the trolleybus has been accelerated to.

        """
        if speed <= self.max_speed:
            return speed
