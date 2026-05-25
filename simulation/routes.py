class Route:

    def __init__(
        self,
        stops,
        route_type,
        frequency=10,
        express=False
    ):

        self.stops = stops

        self.route_type = route_type

        self.frequency = frequency

        self.express = express

        self.stop_count = len(stops)

        self.unique_stops = len(set(stops))

        # =====================================
        # NEW
        # =====================================

        self.travel_time = 0

    def __repr__(self):

        return (
            f"\nRoute(\n"
            f"  type={self.route_type},\n"
            f"  stops={self.stop_count},\n"
            f"  frequency={self.frequency},\n"
            f"  travel_time={self.travel_time}\n"
            f")"
        )