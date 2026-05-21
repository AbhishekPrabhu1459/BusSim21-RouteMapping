from optimization.network_optimizer import (
    optimize_network
)

routes = optimize_network()

print("\n=== GENERATED TRANSIT NETWORK ===\n")

for i, route in enumerate(routes):

    print(f"LINE {i + 1}")
    print(f"Type: {route.route_type}")
    print(f"Stops ({len(route.stops)}):")

    for stop in route.stops:

        print(f" - {stop}")

    print()