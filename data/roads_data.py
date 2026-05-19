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
]