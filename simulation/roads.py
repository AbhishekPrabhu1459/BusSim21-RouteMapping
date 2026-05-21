class Road:

    def __init__(
        self,
        start,
        end,
        distance,
        traffic,
        road_type
    ):

        self.start = start

        self.end = end

        self.distance = distance

        self.traffic = traffic

        self.road_type = road_type


    def __repr__(self):

        return f"{self.start} -> {self.end}"