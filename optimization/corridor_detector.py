from data.demand_data import demand_data


def detect_major_corridors():

    corridors = []

    for (origin, destination), demand in demand_data.items():

        if demand >= 1000:

            corridors.append({
                "origin": origin,
                "destination": destination,
                "demand": demand
            })

    corridors.sort(
        key=lambda x: x["demand"],
        reverse=True
    )

    return corridors