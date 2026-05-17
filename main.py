from data.bus_data import buses

from optimization.network_generator import (
    generate_route_network
)

from optimization.network_scoring import (
    calculate_network_score
)

routes = generate_route_network(len(buses))

score = calculate_network_score(routes)

for i, route in enumerate(routes):

    print(f"Route {i + 1}: {route}")

print()
print("NETWORK SCORE:", score)