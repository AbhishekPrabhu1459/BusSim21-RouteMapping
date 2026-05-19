from simulation.roads import Road


roads = [

    # =====================================
    # MAIN LOOP
    # =====================================

    Road(
        "Media Centre Astra",
        "Stocker Square",
        2,
        0.3,
        "local"
    ),

    Road(
        "Stocker Square",
        "South Spoke",
        2,
        0.4,
        "local"
    ),

    Road(
        "South Spoke",
        "North Spoke",
        2,
        0.3,
        "local"
    ),

    Road(
        "North Spoke",
        "Zellerman Research Center",
        2,
        0.4,
        "local"
    ),

    Road(
        "Zellerman Research Center",
        "Astra Promenade",
        2,
        0.3,
        "local"
    ),

    Road(
        "Astra Promenade",
        "Greens Square",
        2,
        0.3,
        "local"
    ),

    Road(
        "Greens Square",
        "Media Centre Astra",
        2,
        0.3,
        "local"
    ),

    # =====================================
    # EAST BRANCH
    # =====================================

    Road(
        "South Spoke",
        "East Spoke",
        2,
        0.3,
        "local"
    ),

    Road(
        "East Spoke",
        "Zellerman Research Center",
        2,
        0.3,
        "local"
    ),

    Road(
        "East Spoke",
        "Astra Promenade",
        2,
        0.3,
        "local"
    ),

    # =====================================
    # WEST BRANCH
    # =====================================

    Road(
        "South Spoke",
        "West Spoke",
        2,
        0.3,
        "local"
    ),

    Road(
        "West Spoke",
        "Zellerman Research Center",
        2,
        0.4,
        "local"
    ),

    # =====================================
    # SIEGWALDEN ROADS
    # =====================================

    Road(
        "Siegwalden Lido",
        "Siegwalden",
        3,
        0.3,
        "local"
    ),

    Road(
        "Siegwalden",
        "Siegwalden Secondary School",
        2,
        0.3,
        "local"
    ),

    # =====================================
    # INTER-SUBURB CONNECTION
    # =====================================

    Road(
        "Media Centre Astra",
        "Siegwalden Lido",
        4,
        0.5,
        "connector"
    ),
    # =====================================
    # OAKVILLE ROADS
    # =====================================

    Road(
        "Oakville Central",
        "Oak Street",
        2,
        0.3,
        "local"
    ),

    Road(
        "Oak Street",
        "Old Sawmill",
        3,
        0.4,
        "local"
    ),

    # =====================================
    # INTER-SUBURB CONNECTION
    # =====================================

    Road(
        "Siegwalden Secondary School",
        "Oakville Central",
        4,
        0.5,
        "connector"
    ),

    # =====================================
    # INDUSTRIAL ZONE ROADS
    # =====================================

    Road(
        "Shipwrights Alley",
        "Boos Corp Warehouses",
        2,
        0.5,
        "industrial"
    ),

    Road(
        "Boos Corp Warehouses",
        "Water Treatment Plant",
        2,
        0.5,
        "industrial"
    ),

    Road(
        "Water Treatment Plant",
        "Harbour Distribution Centre",
        3,
        0.4,
        "industrial"
    ),

    # =====================================
    # ASTRA CONNECTIONS
    # =====================================

    Road(
        "Media Centre Astra",
        "Boos Corp Warehouses",
        4,
        0.6,
        "connector"
    ),

    Road(
        "Media Centre Astra",
        "Shipwrights Alley",
        5,
        0.7,
        "connector"
    ),
    # =====================================
    # HARBOUR ROADS
    # =====================================

    Road(
        "Harbour Administration",
        "Ressel Warehouse",
        2,
        0.5,
        "harbor"
    ),

    Road(
        "Ressel Warehouse",
        "Harbor Pier 1",
        2,
        0.5,
        "harbor"
    ),

    Road(
        "Harbor Pier 1",
        "Harbor Pier 3",
        2,
        0.6,
        "harbor"
    ),

    Road(
        "Harbor Pier 3",
        "Oil Harbor North",
        3,
        0.6,
        "harbor"
    ),

    Road(
        "Oil Harbor North",
        "Oil Harbor South",
        2,
        0.5,
        "harbor"
    ),

    Road(
        "Oil Harbor South",
        "Harbour Administration",
        4,
        0.5,
        "harbor"
    ),

    # =====================================
    # INDUSTRIAL CONNECTIONS
    # =====================================

    Road(
        "Harbour Distribution Centre",
        "Harbour Administration",
        4,
        0.7,
        "connector"
    ),

    Road(
        "Water Treatment Plant",
        "Harbour Administration",
        5,
        0.7,
        "connector"
    ),
    # =====================================
    # KERSTSTADT ROADS
    # =====================================

    Road(
        "Tyson Planetarium",
        "Ministry of Science",
        2,
        0.4,
        "urban"
    ),

    Road(
        "Ministry of Science",
        "Grain Lane",
        2,
        0.5,
        "urban"
    ),

    Road(
        "Grain Lane",
        "Wachowski Industries",
        2,
        0.5,
        "urban"
    ),

    Road(
        "Wachowski Industries",
        "Arcos Road",
        2,
        0.4,
        "urban"
    ),

    Road(
        "Arcos Road",
        "Kerststadt Church",
        2,
        0.4,
        "urban"
    ),

    Road(
        "Kerststadt Church",
        "Hill Road",
        2,
        0.3,
        "urban"
    ),

    Road(
        "Hill Road",
        "Fruehauf Academy",
        2,
        0.3,
        "urban"
    ),

    Road(
        "Fruehauf Academy",
        "University of Technology",
        2,
        0.5,
        "urban"
    ),

    Road(
        "University of Technology",
        "Grain Lane",
        2,
        0.5,
        "urban"
    ),

    Road(
        "Grain Lane",
        "Winfield East",
        2,
        0.3,
        "urban"
    ),

    Road(
        "Winfield East",
        "Winfield West",
        2,
        0.3,
        "urban"
    ),

    # =====================================
    # BRANCHES
    # =====================================

    Road(
        "Grain Lane",
        "Kerststadt Church",
        2,
        0.4,
        "urban"
    ),

    Road(
        "Kerststadt Church",
        "University of Technology",
        2,
        0.4,
        "urban"
    ),

    Road(
        "Grain Lane",
        "Hill Road",
        2,
        0.3,
        "urban"
    ),

    Road(
        "Hill Road",
        "Tyson Planetarium",
        2,
        0.3,
        "urban"
    ),

    Road(
        "Hill Road",
        "Fruehauf Academy",
        2,
        0.3,
        "urban"
    ),

    Road(
        "Fruehauf Academy",
        "Arcos Road",
        2,
        0.3,
        "urban"
    ),

    Road(
        "Wachowski Industries",
        "Winfield East",
        2,
        0.4,
        "urban"
    ),

    # =====================================
    # INDUSTRIAL CONNECTION
    # =====================================

    Road(
        "Boos Corp Warehouses",
        "Wachowski Industries",
        4,
        0.6,
        "connector"
    ),
]