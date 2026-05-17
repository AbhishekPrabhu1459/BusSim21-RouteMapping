class BusStop:
    def __init__(self, name, zone_type):
        self.name = name
        self.zone_type = zone_type

    def __repr__(self):
        return f"BusStop({self.name}, {self.zone_type})"