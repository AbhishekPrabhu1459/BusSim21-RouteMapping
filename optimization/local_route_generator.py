import random
import networkx as nx

from simulation.city_graph import city_graph
from simulation.routes import Route

from data.stops_data import stops
from data.hub_data import suburb_hubs
from data.district_connections import (
    district_connections
)
from data.district_data import districts


# =====================================
# GET STOPS BY DISTRICT
# =====================================

district_stop_map = {}

for stop in stops:

    district_stop_map.setdefault(
        stop.district,
        []
    ).append(stop.name)


# =====================================
# GENERATE LONG LOCAL ROUTES
# =====================================

def generate_local_routes():

    routes = []

    for district, info in districts.items():

        target_size = info["target_stops"]

        neighbors = district_connections.get(
            district,
            []
        )

        if district not in district_stop_map:
            continue

        local_stops = list(
            district_stop_map[district]
        )

        route_stops = []

        visited_districts = set()

        current_district = district

        while len(route_stops) < target_size:

            if current_district in visited_districts:
                break

            visited_districts.add(
                current_district
            )

            current_stops = district_stop_map.get(
                current_district,
                []
            )

            for stop in current_stops:

                if stop not in route_stops:

                    route_stops.append(stop)

            possible = district_connections.get(
                current_district,
                []
            )

            if not possible:
                break

            current_district = random.choice(
                possible
            )

        # =====================================
        # BUILD CONTINUOUS PATH
        # =====================================

        final_path = []

        for i in range(len(route_stops) - 1):

            try:

                segment = nx.shortest_path(
                    city_graph,
                    route_stops[i],
                    route_stops[i + 1]
                )

                if final_path:
                    segment = segment[1:]

                final_path.extend(segment)

            except:
                pass

        # =====================================
        # ENSURE GOOD ROUTE SIZE
        # =====================================

        if len(final_path) >= 15:

            routes.append(
                Route(
                    final_path,
                    "local"
                )
            )

    return routes