from Trolleybus import Trolleybus

if __name__ == '__main__':
    trolleybuses = [Trolleybus(),
                    Trolleybus(122, "Sknylivok", 70.0, 50, 42),
                    Trolleybus.get_instance(),
                    Trolleybus.get_instance()]

    for trolleybus in trolleybuses:
        print(trolleybus)
        d = getattr(trolleybus, "max_speed")