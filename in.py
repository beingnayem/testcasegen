t = int(input())


for case in range(t):
    n, B = map(int, input().split())


    city_cost = {}     # Stores the lowest cost for each city
    city_order = []    # Tracks first appearance order


    for _ in range(n):
        name, cost = input().split()
        cost = int(cost)


        if name not in city_cost:
            city_cost[name] = cost
            city_order.append(name)
        else:
            city_cost[name] = min(city_cost[name], cost)


    result = []
    for city in city_order:
        if city_cost[city] <= B:
            result.append((city, city_cost[city]))

    
    if result:
        for name, cost in result:
            print(name, cost)
    else:
        print("No City Available")

    if case < t-1:
        print()