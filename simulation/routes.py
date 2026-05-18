class Route:

    def __init__(
        self,
        stops,
        route_type
    ):

        self.stops = stops

        self.route_type = route_type

    def __repr__(self):

        return (
            f"Route("
            f"{self.route_type}: "
            f"{self.stops})"
        )
