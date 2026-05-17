from data.bus_data import buses

from optimization.connected_network_generator import (
    generate_connected_network
)

from optimization.network_scoring import (
    calculate_network_score
)

# ==================================================
# GENERATE CONNECTED TRANSIT NETWORK
# ==================================================

routes = generate_connected_network(
    len(buses)
)

# ==================================================
# CALCULATE NETWORK SCORE
# ==================================================

score = calculate_network_score(routes)

# ==================================================
# ASSIGN ROUTES TO BUSES
# ==================================================

for bus, route in zip(buses, routes):

    bus.assign_route(route)

# ==================================================
# OUTPUT RESULTS
# ==================================================

print()
print("=== GENERATED TRANSIT NETWORK ===")
print()

for bus in buses:

    print(
        f"Bus {bus.bus_id} "
        f"(Capacity: {bus.capacity})"
    )

    print(f"Route: {bus.route.stops}")

    print()

print("NETWORK SCORE:", score)
print()