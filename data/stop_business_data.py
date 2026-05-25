from data.stops_data import stops


business_profiles = {}


for stop in stops:

    profile = {

        "commercial": 1,

        "commuter": 1,

        "tourism": 0,

        "education": 0,

        "industrial": 0
    }

    name = stop.name.lower()

    # =====================================
    # COMMERCIAL
    # =====================================

    if (

        "central" in name
        or "station" in name
        or "trading" in name
        or "town hall" in name
        or "city center" in name

    ):

        profile["commercial"] += 5

        profile["commuter"] += 4

    # =====================================
    # EDUCATION
    # =====================================

    if (

        "school" in name
        or "academy" in name
        or "university" in name
        or "research" in name

    ):

        profile["education"] += 6

        profile["commuter"] += 3

    # =====================================
    # INDUSTRIAL
    # =====================================

    if (

        "warehouse" in name
        or "harbour" in name
        or "industrial" in name
        or "mill" in name
        or "ship" in name
        or "treatment" in name

    ):

        profile["industrial"] += 6

        profile["commuter"] += 5

    # =====================================
    # TOURISM
    # =====================================

    if (

        "park" in name
        or "cathedral" in name
        or "promenade" in name
        or "theatre" in name
        or "planetarium" in name

    ):

        profile["tourism"] += 5

    business_profiles[stop.name] = profile