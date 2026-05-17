class Road:
    def __init__(self, from_stop, to_stop, travel_time, traffic_level):
        self.from_stop = from_stop
        self.to_stop = to_stop
        self.travel_time = travel_time
        self.traffic_level = traffic_level

    def __repr__(self):
        return (
            f"Road({self.from_stop} -> "
            f"{self.to_stop}, {self.travel_time} min)"
        )