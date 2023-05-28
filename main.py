"""
This is file with main.
"""
from models.bicycle import Bicycle
from models.car import Car
from models.tram import Tram
from models.trolleybus import Trolleybus
from managers.transport_manager import TransportManager
from managers.set_manager import SetManager

if __name__ == '__main__':
    transport_manager = TransportManager()
    transport_manager.add_transport(Trolleybus(122, 65, 22, "Sknylivok", 50, 34))
    transport_manager.add_transport(Trolleybus(564, 65, 38, "Kulparkiv", 60, 6))
    transport_manager.add_transport(Car(5680, 250, 2, 450, 22))
    transport_manager.add_transport(Tram(1178, 80, 1, 200))
    transport_manager.add_transport(Tram(1166, 70, 4, 154))
    transport_manager.add_transport(Bicycle(578, 50, "Merida"))
    transport_manager.add_transport(Bicycle(247, 40, "Kellys"))

    car1 = Car(2414, 200, 4, 300, 11)
    transport_manager.add_transport(car1)

    for transport in transport_manager.transports:
        print(transport)

    transport_with_max_speed_higher_than = \
        transport_manager.find_transport_with_max_speed_higher_than(60)
    print("\nTransport with max speed higher than 60:")
    for transport in transport_with_max_speed_higher_than:
        print(transport)

    transport_with_id = transport_manager.find_transport_by_id(564)
    print("\nTransport with id 564:")
    for transport in transport_with_id:
        print(transport)

    print("\nNumber of transports:", len(transport_manager))

    enumeration = transport_manager.get_enumerate()
    print("\nEnumeration of transports:")
    for i, transport in enumeration:
        print(i, transport)

    max_speed = 65
    result = transport_manager.find_transport_by_max_speed(max_speed)
    print(f"\nDo all transports have max speed {max_speed}? {result['all']}")
    print(f"Do any transports have max speed {max_speed}? {result['any']}")

    int_attributes = car1.get_attributes_by_type(int)
    print("\nAttributes with integer values:")
    for attr, value in int_attributes.items():
        print(f"{attr}: {value}")

    set_manager = SetManager(transport_manager)
    print("\nIterating over transports:")
    for item in set_manager:
        print(item)
