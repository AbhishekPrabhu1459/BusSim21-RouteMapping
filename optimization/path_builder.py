import networkx as nx

from simulation.city_graph import city_graph


def build_clean_path(stop_sequence):

    final_path = []

    visited = set()

    for i in range(len(stop_sequence) - 1):

        try:

            segment = nx.shortest_path(

                city_graph,

                stop_sequence[i],

                stop_sequence[i + 1]
            )

            if final_path:

                segment = segment[1:]

            for stop in segment:

                if stop not in visited:

                    final_path.append(stop)

                    visited.add(stop)

        except:

            pass

    return final_path