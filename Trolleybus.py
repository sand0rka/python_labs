class Trolleybus:
    """
    A class representing a trolleybus.

    Attributes:
        __id (int): unique identifier of the trolleybus, the default value is 100;
        __route_number (int): number of the route on which the trolley runs;
        __current_stop (String): the current stop at which the trolleybus is located;
        __max_speed (float): the maximum speed of the trolleybus;
        __capacity (int): the capacity of the trolleybus (the number of passengers that the trolleybus can carry);
        __passengers (int): the current number of passengers carried by the trolleybus.

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

    def __init__(self, route_number=0, current_stop="", max_speed=0.0, capacity=0, passengers=0):
        self.__id = 100
        self.__route_number = route_number
        self.__current_stop = current_stop
        self.__max_speed = max_speed
        self.__capacity = capacity
        self.__passengers = passengers

    def stop(self):
        current_speed = 0.0

    def start(self):
        current_speed = 0.0

    def add_passenger(self):
        if self.__passengers < self.__capacity:
            self.__passengers += 1

    def remove_passenger(self):
        if self.__passengers > 0:
            self.__passengers -= 1

    def __str__(self):
        return f"Trolleybus(id={self.__id}, routeNumber={self.__route_number}, currentStop='{self.__current_stop}', " \
               f"maxSpeed={self.__max_speed}, capacity={self.__capacity}, passengers={self.__passengers})"

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value):
        self.__id = value

    @property
    def route_number(self):
        return self.__route_number

    @route_number.setter
    def route_number(self, value):
        self.__route_number = value

    @property
    def current_stop(self):
        return self.__current_stop

    @current_stop.setter
    def current_stop(self, value):
        self.__current_stop = value

    @property
    def max_speed(self):
        return self.__max_speed

    @max_speed.setter
    def max_speed(self, value):
        self.__max_speed = value

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        self.__capacity = value

    @property
    def passengers(self):
        return self.__passengers

    @passengers.setter
    def passengers(self, value):
        self.__passengers = value

    @staticmethod
    def get_instance():
        if Trolleybus.default_trolleybus is None:
            Trolleybus.default_trolleybus = Trolleybus()
        return Trolleybus.default_trolleybus


if __name__ == '__main__':
    trolleybuses = [Trolleybus(),
                    Trolleybus(122, "Sknylivok", 70.0, 50, 42),
                    Trolleybus.get_instance(),
                    Trolleybus.get_instance()]

    for trolleybus in trolleybuses:
        print(trolleybus)
