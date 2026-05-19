demand_data = {

    # =====================================
    # INTERNAL DEMAND
    # =====================================

    ("Astra Park", "Astra Park"): 1000,

    ("Siegwalden", "Siegwalden"): 400,

    ("Oakville", "Oakville"): 300,

    ("Industrial Zone", "Industrial Zone"): 500,

    ("Harbour", "Harbour"): 450,

    ("Kerststadt", "Kerststadt"): 1200,

    ("Agricultural Zone", "Agricultural Zone"): 250,

    ("Sonnstein", "Sonnstein"): 350,

    # =====================================
    # COMMUTER DEMAND
    # =====================================

    ("Oakville", "Astra Park"): 450,

    ("Oakville", "Siegwalden"): 500,

    ("Siegwalden", "Astra Park"): 700,

    ("Astra Park", "Siegwalden"): 650,

    # =====================================
    # INDUSTRIAL COMMUTING
    # =====================================

    ("Astra Park", "Industrial Zone"): 900,

    ("Siegwalden", "Industrial Zone"): 600,

    ("Oakville", "Industrial Zone"): 500,

    # =====================================
    # HARBOUR COMMUTING
    # =====================================

    ("Astra Park", "Harbour"): 850,

    ("Industrial Zone", "Harbour"): 950,

    ("Siegwalden", "Harbour"): 500,

    ("Oakville", "Harbour"): 450,

    # =====================================
    # UNIVERSITY COMMUTING
    # =====================================

    ("Astra Park", "Kerststadt"): 1100,

    ("Industrial Zone", "Kerststadt"): 900,

    ("Siegwalden", "Kerststadt"): 700,

    ("Oakville", "Kerststadt"): 650,

    ("Harbour", "Kerststadt"): 500,

    # =====================================
    # AGRICULTURAL FLOW
    # =====================================

    ("Agricultural Zone", "Industrial Zone"): 700,

    ("Agricultural Zone", "Harbour"): 500,

    ("Astra Park", "Agricultural Zone"): 250,

    ("Kerststadt", "Agricultural Zone"): 200,

    # =====================================
    # SONNSTEIN COMMUTING
    # =====================================

    ("Sonnstein", "Kerststadt"): 850,

    ("Sonnstein", "Industrial Zone"): 500,

    ("Sonnstein", "Harbour"): 350,

    ("Sonnstein", "Astra Park"): 400,
}