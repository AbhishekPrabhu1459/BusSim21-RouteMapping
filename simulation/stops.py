class BusStop:

    def __init__(
        self,
        name,
        zone_type,
        suburb,
        district_type,
        hub_level=0
    ):

        self.name = name

        self.zone_type = zone_type

        self.suburb = suburb

        self.district_type = district_type

        self.hub_level = hub_level

    def __repr__(self):

        return (
            f"BusStop("
            f"{self.name}, "
            f"{self.suburb}, "
            f"hub={self.hub_level})"
        )
