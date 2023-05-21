from .Transport import Transport


class Trolleybus(Transport):
    """
    A class representing a trolleybus.

    Attributes:
        id (int): unique identifier of the trolleybus, the default value is 100;
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

    def __init__(self, id=100, max_speed=0.0, route_number=0, current_stop="", capacity=0, passengers=0):
        super().__init__(id, max_speed)
        self.route_number = route_number
        self.current_stop = current_stop
        self.max_speed = max_speed
        self.capacity = capacity
        self.passengers = passengers

    def __cmp__(self, other):
        return self.route_number == other.route_number and self.current_stop == other.current_stop and \
                self.max_speed == other.max_speed and self.capacity == other.capacity and \
                self.passengers == other.passengers

    def stop(self):
        self.accelerate(0)

    def start(self):
        self.accelerate(20)

    def add_passenger(self):
        if self.passengers < self.capacity:
            self.passengers += 1

    def remove_passenger(self):
        if self.passengers > 0:
            self.passengers -= 1

    def __str__(self):
        return f"Trolleybus(id={self.id}, max_speed={self.max_speed}, route_number={self.route_number}, " \
               f"current_stop='{self.current_stop}',  capacity={self.capacity}, passengers={self.passengers})"

    @staticmethod
    def get_instance():
        if Trolleybus.default_trolleybus is None:
            Trolleybus.default_trolleybus = Trolleybus()
        return Trolleybus.default_trolleybus

    def accelerate(self, speed):
        return speed
