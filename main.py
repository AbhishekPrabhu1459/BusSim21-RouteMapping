from data.bus_data import buses

from optimization.network_generator import (
    generate_route_network
)

from optimization.network_scoring import (
    calculate_network_score
)

# =========================================
# GENERATE OPTIMIZED ROUTES
# =========================================

routes = generate_route_network()

# =========================================
# ASSIGN ONLY NECESSARY BUSES
# =========================================

required_buses = min(
    len(routes),
    len(buses)
)

for i in range(required_buses):

    buses[i].assign_route(
        routes[i]
    )

# =========================================
# CALCULATE NETWORK SCORE
# =========================================

score = calculate_network_score(routes)

# =========================================
# OUTPUT ACTIVE BUSES
# =========================================

print()
print("=== ACTIVE BUSES ===")
print()

for i in range(required_buses):

    bus = buses[i]

    print(
        f"Bus {bus.bus_id}"
    )

    print(
        f"Capacity: {bus.capacity}"
    )

    print(
        f"Route Type: "
        f"{bus.route.route_type}"
    )

    print(
        f"Route: "
        f"{bus.route.stops}"
    )

    print()

# =========================================
# OUTPUT UNUSED BUSES
# =========================================

unused_buses = buses[required_buses:]

print()
print("=== UNUSED BUSES ===")
print()

if unused_buses:

    for bus in unused_buses:

        print(
            f"Bus {bus.bus_id} unused"
        )

else:

    print("No unused buses")

# =========================================
# NETWORK SCORE
# =========================================

print()
print("NETWORK SCORE:", score)
print()