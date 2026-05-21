class BusStop:

    def __init__(
        self,
        name,
        stop_type,
        district,
        district_type,
        hub_level=1
    ):

        self.name = name

        self.stop_type = stop_type

        self.district = district

        self.district_type = district_type

        self.hub_level = hub_level


    def __repr__(self):

        return f"{self.name}"