from simulation.stops import BusStop


stops = [

    # =====================================
    # ASTRA PARK
    # =====================================

    BusStop(
        "Media Centre Astra",
        "commercial",
        "Astra Park",
        "suburban",
        hub_level=9
    ),

    BusStop(
        "Stocker Square",
        "commercial",
        "Astra Park",
        "suburban",
        hub_level=6
    ),

    BusStop(
        "South Spoke",
        "residential",
        "Astra Park",
        "suburban",
        hub_level=7
    ),

    BusStop(
        "North Spoke",
        "residential",
        "Astra Park",
        "suburban",
        hub_level=5
    ),

    BusStop(
        "East Spoke",
        "residential",
        "Astra Park",
        "suburban",
        hub_level=4
    ),

    BusStop(
        "West Spoke",
        "residential",
        "Astra Park",
        "suburban",
        hub_level=4
    ),

    BusStop(
        "Zellerman Research Center",
        "education",
        "Astra Park",
        "suburban",
        hub_level=8
    ),

    BusStop(
        "Astra Promenade",
        "commercial",
        "Astra Park",
        "suburban",
        hub_level=5
    ),

    BusStop(
        "Greens Square",
        "commercial",
        "Astra Park",
        "suburban",
        hub_level=6
    ),
    # =====================================
    # SIEGWALDEN
    # =====================================

    BusStop(
        "Siegwalden",
        "commercial",
        "Siegwalden",
        "suburban",
        hub_level=8
    ),

    BusStop(
        "Siegwalden Lido",
        "recreation",
        "Siegwalden",
        "suburban",
        hub_level=6
    ),

    BusStop(
        "Siegwalden Secondary School",
        "education",
        "Siegwalden",
        "suburban",
        hub_level=5
    ),
    # =====================================
    # OAKVILLE
    # =====================================

    BusStop(
        "Oakville Central",
        "commercial",
        "Oakville",
        "suburban",
        hub_level=7
    ),

    BusStop(
        "Oak Street",
        "residential",
        "Oakville",
        "suburban",
        hub_level=4
    ),

    BusStop(
        "Old Sawmill",
        "industrial",
        "Oakville",
        "suburban",
        hub_level=5
    ),
    # =====================================
    # INDUSTRIAL ZONE
    # =====================================

    BusStop(
        "Harbour Distribution Centre",
        "industrial",
        "Industrial Zone",
        "industrial",
        hub_level=10
    ),

    BusStop(
        "Boos Corp Warehouses",
        "industrial",
        "Industrial Zone",
        "industrial",
        hub_level=7
    ),

    BusStop(
        "Water Treatment Plant",
        "industrial",
        "Industrial Zone",
        "industrial",
        hub_level=5
    ),

    BusStop(
        "Shipwrights Alley",
        "industrial",
        "Industrial Zone",
        "industrial",
        hub_level=6
    ),
    # =====================================
    # HARBOUR
    # =====================================

    BusStop(
        "Harbour Administration",
        "commercial",
        "Harbour",
        "harbor",
        hub_level=10
    ),

    BusStop(
        "Ressel Warehouse",
        "industrial",
        "Harbour",
        "harbor",
        hub_level=7
    ),

    BusStop(
        "Harbor Pier 1",
        "industrial",
        "Harbour",
        "harbor",
        hub_level=6
    ),

    BusStop(
        "Harbor Pier 3",
        "industrial",
        "Harbour",
        "harbor",
        hub_level=6
    ),

    BusStop(
        "Oil Harbor North",
        "industrial",
        "Harbour",
        "harbor",
        hub_level=5
    ),

    BusStop(
        "Oil Harbor South",
        "industrial",
        "Harbour",
        "harbor",
        hub_level=5
    ),
    # =====================================
    # KERSTSTADT
    # =====================================

    BusStop(
        "University of Technology",
        "education",
        "Kerststadt",
        "university",
        hub_level=10
    ),

    BusStop(
        "Grain Lane",
        "commercial",
        "Kerststadt",
        "university",
        hub_level=8
    ),

    BusStop(
        "Wachowski Industries",
        "industrial",
        "Kerststadt",
        "university",
        hub_level=7
    ),

    BusStop(
        "Tyson Planetarium",
        "education",
        "Kerststadt",
        "university",
        hub_level=6
    ),

    BusStop(
        "Ministry of Science",
        "government",
        "Kerststadt",
        "university",
        hub_level=6
    ),

    BusStop(
        "Arcos Road",
        "commercial",
        "Kerststadt",
        "university",
        hub_level=5
    ),

    BusStop(
        "Kerststadt Church",
        "commercial",
        "Kerststadt",
        "university",
        hub_level=5
    ),

    BusStop(
        "Hill Road",
        "residential",
        "Kerststadt",
        "university",
        hub_level=5
    ),

    BusStop(
        "Fruehauf Academy",
        "education",
        "Kerststadt",
        "university",
        hub_level=6
    ),

    BusStop(
        "Winfield East",
        "residential",
        "Kerststadt",
        "university",
        hub_level=4
    ),

    BusStop(
        "Winfield West",
        "residential",
        "Kerststadt",
        "university",
        hub_level=4
    ),
    # =====================================
    # AGRICULTURAL ZONE
    # =====================================

    BusStop(
        "Corn Street Agriculture Centre",
        "industrial",
        "Agricultural Zone",
        "regional",
        hub_level=8
    ),

    BusStop(
        "Nutrivore Research Labs",
        "education",
        "Agricultural Zone",
        "regional",
        hub_level=6
    ),

    BusStop(
        "Sugar Mill",
        "industrial",
        "Agricultural Zone",
        "regional",
        hub_level=5
    ),

    BusStop(
        "Hay Scales",
        "industrial",
        "Agricultural Zone",
        "regional",
        hub_level=4
    ),
    # =====================================
    # SONNSTEIN
    # =====================================

    BusStop(
        "Sonnstein Main Square",
        "commercial",
        "Sonnstein",
        "regional",
        hub_level=8
    ),

    BusStop(
        "Miller Road",
        "residential",
        "Sonnstein",
        "regional",
        hub_level=6
    ),

    BusStop(
        "Sonnleitner Farm",
        "industrial",
        "Sonnstein",
        "regional",
        hub_level=5
    ),

    BusStop(
        "Cellar Road",
        "commercial",
        "Sonnstein",
        "regional",
        hub_level=4
    ),

    BusStop(
        "Soon Mautner Farm",
        "industrial",
        "Sonnstein",
        "regional",
        hub_level=5
    ),

    BusStop(
        "Lower Sonnstein",
        "residential",
        "Sonnstein",
        "regional",
        hub_level=6
    ),

    BusStop(
        "Sun Road",
        "residential",
        "Sonnstein",
        "regional",
        hub_level=4
    ),
]