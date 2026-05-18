class Road:

    def __init__(
        self,
        from_stop,
        to_stop,
        travel_time,
        traffic_level,
        road_type="standard"
    ):

        self.from_stop = from_stop

        self.to_stop = to_stop

        self.travel_time = travel_time

        self.traffic_level = traffic_level

        self.road_type = road_type

    def __repr__(self):

        return (
            f"Road("
            f"{self.from_stop} -> "
            f"{self.to_stop}, "
            f"{self.road_type})"
        )