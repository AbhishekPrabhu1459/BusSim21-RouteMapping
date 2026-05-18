import networkx as nx

from data.stops_data import stops
from data.roads_data import roads


city_graph = nx.Graph()


for stop in stops:

    city_graph.add_node(
        stop.name,
        zone_type=stop.zone_type,
        suburb=stop.suburb,
        district_type=stop.district_type,
        hub_level=stop.hub_level
    )


for road in roads:

    city_graph.add_edge(
        road.from_stop,
        road.to_stop,
        travel_time=road.travel_time,
        traffic=road.traffic_level,
        road_type=road.road_type
    )
