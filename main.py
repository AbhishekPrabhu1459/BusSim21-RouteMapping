from optimization.route_generator import generate_random_route
from optimization.scoring import calculate_route_score

best_route = None
best_score = -1

for _ in range(100):

    route = generate_random_route()

    score = calculate_route_score(route)

    if score > best_score:
        best_score = score
        best_route = route

print("BEST ROUTE:")
print(best_route)
print(best_score)