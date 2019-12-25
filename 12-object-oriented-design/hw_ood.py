class Building:
    def __init__(self, name, **kwargs):
        self.storage = []
        self.name = name


class Warehouse(Building):
    def __init__(self, name, delivery_time):
        super().__init__(name)
        self.delivery_time = delivery_time

    def delivered(self, number_of_containers):
        return len(self.storage) == number_of_containers

    def get_cargo(self, container):
        self.storage.append(container)


class Transport:
    def __init__(self, name):
        self.destination = None
        self.time = 0
        self.at_the_factory = True
        self.cargo = None
        self.name = name

    def move(self, destination: Warehouse, cargo):
        self.destination = destination
        self.time = 2 * destination.delivery_time
        self.at_the_factory = False
        self.cargo = cargo

    def stage(self):
        if self.at_the_factory:
            return
        self.time -= 1
        if self.time == self.destination.delivery_time:
            self.destination.get_cargo(self.cargo)
        if self.time == 0:
            self.at_the_factory = True


class Factory(Building):
    def __init__(self, name, containers, transport: list, warehouses, **kwargs):
        super().__init__(name, **kwargs)
        self.storage = list(containers)
        self.transport = transport
        self.warehouses = warehouses

    def delivery(self):
        for transport in self.transport:
            if transport.at_the_factory:
                if self.storage:
                    container = self.storage.pop(0)
                    transport.move(self.warehouses[container], container)


class Port(Factory, Warehouse):
    pass


if __name__ == '__main__':
    containers = input('Input list of cargoes: ')
    ship = Transport('Ship')
    truck1 = Transport('Truck 1')
    truck2 = Transport('Truck 2')
    warehouseA = Warehouse('A', 4)
    warehouseB = Warehouse('B', 5)
    port = Port('Port', [], [ship], {'A': warehouseA}, delivery_time=1)
    factory = Factory('Factory', containers, [truck1, truck2], {'A': port, 'B': warehouseB})
    time = 1
    while True:
        factory.delivery()
        port.delivery()
        truck1.stage()
        truck2.stage()
        ship.stage()
        if warehouseA.delivered(containers.count('A')) and warehouseB.delivered(containers.count('B')):
            break
        time += 1
    print(f'Delivery time: {time}')
