class BusStop:

    def __init__(
        self,
        name,
        stop_type,
        district,
        district_type,
        hub_level=1,
        activity_level=None,
        employment_density=None,
        education_score=None,
        tourism_score=None,
        transfer_score=None
    ):

        self.name = name

        self.stop_type = stop_type

        self.district = district

        self.district_type = district_type

        self.hub_level = hub_level

        # =====================================
        # AUTO-GENERATED SMART DEFAULTS
        # =====================================

        self.activity_level = (
            activity_level
            if activity_level is not None
            else self.generate_activity()
        )

        self.employment_density = (
            employment_density
            if employment_density is not None
            else self.generate_employment()
        )

        self.education_score = (
            education_score
            if education_score is not None
            else self.generate_education()
        )

        self.tourism_score = (
            tourism_score
            if tourism_score is not None
            else self.generate_tourism()
        )

        self.transfer_score = (
            transfer_score
            if transfer_score is not None
            else self.generate_transfer()
        )

    # =====================================
    # AUTO GENERATION LOGIC
    # =====================================

    def generate_activity(self):

        score = self.hub_level

        if self.district_type in [
            "CBD",
            "metropolitan_core",
            "urban_core"
        ]:
            score += 4

        if self.stop_type in [
            "commercial",
            "transport",
            "government"
        ]:
            score += 3

        return score

    def generate_employment(self):

        score = 1

        if self.stop_type in [
            "industrial",
            "government",
            "commercial"
        ]:
            score += 5

        if (
            "warehouse" in self.name.lower()
            or "industry" in self.name.lower()
            or "harbour" in self.name.lower()
            or "trading" in self.name.lower()
        ):
            score += 4

        return score

    def generate_education(self):

        score = 0

        if self.stop_type == "education":
            score += 6

        if (
            "school" in self.name.lower()
            or "academy" in self.name.lower()
            or "university" in self.name.lower()
            or "research" in self.name.lower()
        ):
            score += 5

        return score

    def generate_tourism(self):

        score = 0

        if (
            "theatre" in self.name.lower()
            or "cathedral" in self.name.lower()
            or "planetarium" in self.name.lower()
            or "park" in self.name.lower()
            or "promenade" in self.name.lower()
        ):
            score += 6

        return score

    def generate_transfer(self):

        score = self.hub_level

        if self.stop_type == "transport":
            score += 5

        if "station" in self.name.lower():
            score += 4

        return score

    def __repr__(self):

        return f"{self.name}"