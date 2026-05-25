class Road:

    def __init__(

        self,

        start,

        end,

        distance,

        traffic,

        road_type,

        speed_limit=None,

        capacity=None,

        bus_priority=False,

        congestion_factor=None,

        express_suitable=None
    ):

        self.start = start

        self.end = end

        self.distance = distance

        self.traffic = traffic

        self.road_type = road_type

        # =====================================
        # AUTO-GENERATED DEFAULTS
        # =====================================

        self.speed_limit = (
            speed_limit
            if speed_limit is not None
            else self.generate_speed_limit()
        )

        self.capacity = (
            capacity
            if capacity is not None
            else self.generate_capacity()
        )

        self.bus_priority = (
            bus_priority
            if bus_priority is not None
            else self.generate_bus_priority()
        )

        self.congestion_factor = (
            congestion_factor
            if congestion_factor is not None
            else self.generate_congestion()
        )

        self.express_suitable = (
            express_suitable
            if express_suitable is not None
            else self.generate_express_suitable()
        )

    # =====================================
    # AUTO GENERATION
    # =====================================

    def generate_speed_limit(self):

        if self.road_type == "CBD":
            return 30

        if self.road_type in [
            "urban",
            "urban_core"
        ]:
            return 40

        if self.road_type in [
            "suburban",
            "connector"
        ]:
            return 60

        if self.road_type in [
            "regional",
            "industrial"
        ]:
            return 70

        return 50

    def generate_capacity(self):

        if self.road_type == "CBD":
            return 1200

        if self.road_type in [
            "urban_core",
            "urban"
        ]:
            return 1000

        if self.road_type == "connector":
            return 800

        if self.road_type == "regional":
            return 500

        return 700

    def generate_bus_priority(self):

        if self.road_type in [
            "CBD",
            "urban_core",
            "connector"
        ]:
            return True

        return False

    def generate_congestion(self):

        congestion = self.traffic

        if self.road_type == "CBD":
            congestion += 0.4

        if self.road_type == "urban_core":
            congestion += 0.3

        return min(congestion, 1.0)

    def generate_express_suitable(self):

        if self.road_type in [
            "connector",
            "regional"
        ]:

            if self.distance >= 4:
                return True

        return False

    def __repr__(self):

        return f"{self.start} -> {self.end}"