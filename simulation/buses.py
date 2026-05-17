class Bus:
    def __init__(self, bus_id, capacity):
        self.bus_id = bus_id
        self.capacity = capacity
        self.route = None

    def assign_route(self, route):
        self.route = route