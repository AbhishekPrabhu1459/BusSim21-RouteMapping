from simulation.routes import Route

from data.stops_data import stops


district_stop_map = {}


for stop in stops:

    district_stop_map.setdefault(
        stop.district,
        []
    ).append(stop.name)


def generate_local_routes():

    routes = []

    for district, stop_list in district_stop_map.items():

        if len(stop_list) < 4:
            continue

        # =====================================
        # SPLIT INTO 2 LOCAL LOOPS
        # =====================================

        midpoint = len(stop_list) // 2

        route1 = stop_list[:midpoint + 1]

        route2 = stop_list[midpoint:]

        if len(route1) >= 4:

            routes.append(
                Route(
                    route1,
                    "local"
                )
            )

        if len(route2) >= 4:

            routes.append(
                Route(
                    route2,
                    "local"
                )
            )

    return routes