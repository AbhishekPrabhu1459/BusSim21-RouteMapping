import networkx as nx

from data.stops_data import stops
from data.roads_data import roads

city_graph = nx.Graph()

# Add stops as nodes
for stop in stops:
    city_graph.add_node(
        stop.name,
        zone=stop.zone_type
    )

# Add roads as edges
for road in roads:
    city_graph.add_edge(
        road.from_stop,
        road.to_stop,
        travel_time=road.travel_time,
        traffic=road.traffic_level
    )