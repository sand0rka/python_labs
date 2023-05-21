from models.Bicycle import Bicycle
from models.Car import Car
from models.Tram import Tram
from models.Trolleybus import Trolleybus
from managers.TransportManager import TransportManager

if __name__ == '__main__':
    transport_manager = TransportManager()
    transport_manager.add_transport(Trolleybus(122, 65, 22, "Sknylivok", 50, 34))
    transport_manager.add_transport(Trolleybus(564, 60, 38, "Kulparkiv", 60, 6))
    transport_manager.add_transport(Car(2414, 200, 4, 300, 11))
    transport_manager.add_transport(Car(5680, 250, 2, 450, 22))
    transport_manager.add_transport(Tram(1178, 80, 1, 200))
    transport_manager.add_transport(Tram(1166, 70, 4, 154))
    transport_manager.add_transport(Bicycle(247, 40, "Kellys"))
    transport_manager.add_transport(Bicycle(578, 50, "Merida"))

    for transport in transport_manager.transports:
        print(transport)

    transport_with_max_speed_higher_than = transport_manager.find_transport_with_max_speed_higher_than(60)
    print("\nTransport with max speed higher than 60:")
    for transport in transport_with_max_speed_higher_than:
        print(transport)

    transport_with_id = transport_manager.find_transport_by_id(564)
    print("\nTransport with id 564:")
    for transport in transport_with_id:
        print(transport)
