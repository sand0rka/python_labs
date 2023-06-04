"""
This is file with main.
"""
from models.bicycle import Bicycle
from models.car import Car
from models.tram import Tram
from models.trolleybus import Trolleybus
from managers.transport_manager import TransportManager

if __name__ == '__main__':
    transport_manager = TransportManager()
    transport_manager.add_transport(Trolleybus(122, 65, 22, "Sknylivok", 50, 34))
    transport_manager.add_transport(Car(5680, 250, 2, 450, 22))
    transport_manager.add_transport(Tram(1178, 80, 1, 200))
    transport_manager.add_transport(Bicycle(578, 50, "Merida"))

    car1 = Car(2414, 200, 4, 300, 11)
    transport_manager.add_transport(car1)
    car1.accelerate(250)
    tram1 = Tram(1178, 80, 1, 200)
    tram1.accelerate(100)

    transport_with_id = transport_manager.find_transport_by_id(500)

