class Building:
    def __init__(self, name, **kwargs):
        """
        :param name: name of a building
        :param kwargs: kwargs
        """
        self.storage = []
        self.name = name


class Warehouse(Building):
    def __init__(self, deliv_time, **kwargs):
        """
        :param name: name of a building
        :param deliv_time: delivery time needed to get from one point to another
        :param kwargs: name and other kwargs from parent class
        """
        self.deliv_time = deliv_time
        super().__init__(**kwargs)

    def delivery(self, number_of_containers):
        """
        Delivery indicator
        :param number_of_containers: number of containers for delivery
        :return: boolean values, if everything is delivered or not
        """
        return len(self.storage) == number_of_containers

    def add_cargo(self, container):
        """
        Adds container to the suitable storage
        :param container: container type
        :return: None
        """
        self.storage.append(container)
        print(f'Cargo {container} is delivered to the warehouse {self.name}')


class Transport:
    def __init__(self, name):
        """
        :param name: name of transport
        """
        self.name = name
        self.destination = None
        self.cargo = None
        self.starting_point = True
        self.time = 0

    def move(self, destination: Warehouse, cargo):
        """
        Describes transport movement
        :param destination: transport destination with a specific container type
        :param cargo: type of a cargo
        :return: None
        """
        self.destination = destination
        self.cargo = cargo
        self.time = 2 * destination.deliv_time
        self.starting_point = False

    def stage(self):
        """
        Indicate transport location
        """
        if self.starting_point:
            print(f'{self.name} is at the starting point')
            return
        self.time -= 1
        if self.time == self.destination.deliv_time:
            self.destination.add_cargo(self.cargo)
            print(f'{self.name} arrived to destination point')
        elif self.time == 0:
            self.starting_point = True
            print(f'{self.name} returned to the factory')


class Factory(Building):
    def __init__(self, cont, transport: list, warehouses: dict, **kwargs):
        """
        :param cont: chain of containers to be delivered
        :param transport: free transport
        :param warehouses: dict of Building for different types of containers
        :param kwargs: name and other kwargs from parent class
        """
        super().__init__(**kwargs)
        self.storage = list(cont)
        self.transport = transport
        self.warehouses = warehouses

    def assign_delivery(self):
        """
        Logging the assigning of transport for delivery
        """
        for one in self.transport:
            if one.starting_point:
                if self.storage:
                    cont = self.storage.pop(0)
                    one.move(self.warehouses[cont], cont)
                    print(f'{one.name} took cargo {cont} from point {self.name}')
                else:
                    print(f'There is no cargo at point {self.name}')
            else:
                print(f'{one.name} is not at point {self.name}')


class Port(Factory, Warehouse):
    """
    Inherited from Factory
    """
    pass


if __name__ == '__main__':
    containers = input('Input list of cargoes: ')
    truck1 = Transport('Truck 1')
    truck2 = Transport('Truck 2')
    ship = Transport('Ship')
    whA = Warehouse(name='A', deliv_time=4)
    whB = Warehouse(name='B', deliv_time=5)
    port = Port(name='Port', transport=[ship],
                warehouses={'A': whA}, deliv_time=1, cont=[])
    factory = Factory(name='Factory', transport=[truck1, truck2],
                      warehouses={'A': port, 'B': whB},
                      cont=containers)
    time = 1
    while True:
        print(f'\n###############\niteration {time}\n')
        factory.assign_delivery()
        port.assign_delivery()
        truck1.stage()
        truck2.stage()
        ship.stage()
        if whA.delivery(containers.count('A')) and whB.delivery(containers.count('B')):
            break
        time += 1
    print(f'Delivery time: {time}')
