from simulation.routes import Route

from data.stops_data import stops
from data.hub_data import suburb_hubs


district_stop_map = {}


for stop in stops:

    district_stop_map.setdefault(
        stop.district,
        []
    ).append(stop.name)


def generate_local_routes():

    routes = []

    for district, stop_list in district_stop_map.items():

        if len(stop_list) < 6:
            continue

        hub = suburb_hubs[district]["hub"]

        # =====================================
        # ENSURE HUB IS CENTRAL
        # =====================================

        ordered = []

        if hub in stop_list:

            ordered.append(hub)

        for stop in stop_list:

            if stop != hub:

                ordered.append(stop)

        # =====================================
        # SINGLE LARGE LOCAL LOOP
        # =====================================

        if len(ordered) >= 10:

            routes.append(
                Route(
                    ordered,
                    "local"
                )
            )

        else:

            # =====================================
            # SMALL DISTRICTS
            # =====================================

            midpoint = len(ordered) // 2

            route1 = ordered[:midpoint + 1]

            route2 = (
                [hub]
                + ordered[midpoint:]
            )

            if len(route1) >= 6:

                routes.append(
                    Route(
                        route1,
                        "local"
                    )
                )

            if len(route2) >= 6:

                routes.append(
                    Route(
                        route2,
                        "local"
                    )
                )

    return routes