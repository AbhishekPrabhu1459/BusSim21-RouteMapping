import networkx as nx

from data.stops_data import stops
from data.roads_data import roads


city_graph = nx.Graph()


# =====================================
# ADD STOPS
# =====================================

for stop in stops:

    city_graph.add_node(

        stop.name,

        stop_type=stop.stop_type,

        district=stop.district,

        district_type=stop.district_type,

        hub_level=stop.hub_level
    )


# =====================================
# ADD ROADS
# =====================================

for road in roads:

    city_graph.add_edge(

        road.start,

        road.end,

        distance=road.distance,

        traffic=road.traffic,

        road_type=road.road_type
    )