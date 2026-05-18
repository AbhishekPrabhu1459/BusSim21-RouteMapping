from simulation.stops import BusStop


stops = [

    # =====================================
    # OLD TOWN / CBD
    # =====================================

    BusStop(
        "Old Town Central",
        "commercial",
        "Old Town",
        "urban_core",
        hub_level=10
    ),

    BusStop(
        "Old Town East",
        "commercial",
        "Old Town",
        "urban_core",
        hub_level=8
    ),

    BusStop(
        "Old Town South",
        "commercial",
        "Old Town",
        "urban_core",
        hub_level=7
    ),

    # =====================================
    # WESTFIELD
    # =====================================

    BusStop(
        "Westfield Central",
        "residential",
        "Westfield",
        "suburban",
        hub_level=6
    ),

    BusStop(
        "Westfield North",
        "residential",
        "Westfield",
        "suburban"
    ),

    BusStop(
        "Westfield South",
        "residential",
        "Westfield",
        "suburban"
    ),

    # =====================================
    # INDUSTRIAL ZONE
    # =====================================

    BusStop(
        "Industrial Hub",
        "industrial",
        "Industrial Zone",
        "industrial",
        hub_level=9
    ),

    BusStop(
        "Industrial East",
        "industrial",
        "Industrial Zone",
        "industrial"
    ),

    # =====================================
    # AIRPORT
    # =====================================

    BusStop(
        "Airport Terminal",
        "transport",
        "Airport",
        "regional",
        hub_level=8
    ),
]
