class Route:
    def __init__(self, stops):
        self.stops = stops

    def __repr__(self):
        return f"Route({self.stops})"