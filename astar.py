# graph = {"Linz": {"Self": 318, "Passau": 102, "Salzburg": 126}, "Passau": {"Self": 257, "Linz": 102, "Muenchen": 158},
#         "Salzburg": {"Self": 236, "Linz": 126, "Rosenheim": 81}, "Rosenheim": {"Self": 168, "Salzburg": 81, "Muenchen": 59},
#         "Muenchen": {"Self": 120, "Ulm": 123, "Memmingen": 115, "Passau": 158, "Rosenheim": 59},
#         "Ulm": {"Self": 0, "Memmingen": 55, "Muenchen": 123}, "Memmingen": {"Self": 47, "Ulm": 55, "Muenchen": 115}}

graph = {"Arad": {"Self": 366, "Zerind": 75, "Timisoara": 118, "Sibiu": 140}, "Zerind": {"Self": 374, "Arad": 75, "Oradea": 71}, "Timisoara": {"Self": 329, "Arad": 118, "Lugoj": 111},
        "Oradea": {"Self": 380, "Zerind": 71, "Sibiu": 151}, "Lugoj": {"Self": 244, "Timisoara": 111, "Mehadia": 70}, "Sibiu": {"Self": 253, "Oradea": 151, "Arad": 140, "Fagaras": 99, "Rimnicu": 80},
        "Mehadia": {"Self": 241, "Lugoj": 70, "Dobreta": 75}, "Dobreta": {"Self": 242, "Mehadia": 75, "Craiova": 120}, "Rimnicu": {"Self": 193, "Sibiu": 80, "Pitesti": 97, "Craiova": 146},
        "Fagaras": {"Self": 176, "Sibiu": 99, "Bucharest": 211}, "Pitesti": {"Self": 100, "Rimnicu": 97, "Craiova": 138, "Bucharest": 101}, "Bucharest": {"Self": 0, "Pitesti": 101, "Fagaras": 211, "Giurgiu": 90, "Urziceni": 85},
        "Giurgiu": {"Self": 77, "Bucharest": 90}, "Urziceni": {"Self": 80, "Bucharest": 85, "Hirsova": 98, "Vaslui": 142}, "Hirsova": {"Self": 151, "Urziceni": 98, "Eforie": 86}, "Eforie": {"Self": 161, "Hirsova": 86},
        "Vaslui": {"Self": 199, "Iasi": 92, "Urziceni": 142}, "Iasi": {"Self": 226, "Vaslui": 92, "Neamt": 87}, "Neamt": {"Self": 234, "Iasi": 87},
        "Craiova": {"Self": 160, "Dobreta": 120, "Rimnicu": 146, "Pitesti": 138}}

def astar(graph, start, goal):
    graphWhole = graph
    cost_so_far = {}
    tempCostSoFar = 0
    came_from = {}
    visitedCities = [start]
    miniCost, miniCostinCostSoFar = 0, 0
    while start != goal or miniCost != miniCostinCostSoFar:
        graph = graphWhole[start]
        
        # print("Cost so far before", cost_so_far)
        for city, cost in graph.items():
            if city != "Self":

                totalCost = tempCostSoFar + cost + (graphWhole[city])["Self"]
                if city not in cost_so_far or cost_so_far[city] > totalCost:
                    cost_so_far.update({city: totalCost}) #update if the city is not already in cost_so_far / if the city is already there, but its totalCost is bigger
                miniCost = totalCost
                if city not in visitedCities and cost_so_far[city] >= totalCost:
                    came_from.update({city: start})

        # print("Cost so far after", cost_so_far)
        for city, totalCost in cost_so_far.items():
            #Find the minimum
            if miniCost >= totalCost:
                miniCost = totalCost
                miniCity = city

        
        # print("mini City", miniCity)
        tempCostSoFar = cost_so_far[miniCity] - (graphWhole[miniCity])["Self"] #Save the path cost
        start = miniCity
        # print(start)
        visitedCities.append(start)
        key_min = min(cost_so_far.keys(), key=(lambda k: cost_so_far[k]))
        
        # print("Mini cost", miniCost)
        # print("Came from", came_from)
        miniCostinCostSoFar = cost_so_far[key_min] # so that even if the goal is found but it is not yet the minimum cost, we have to keep expanding
        cost_so_far.pop(start)
        # path.append(start)
    
    return came_from, miniCost
    

def reconstruct_path(came_from, start, goal):
    current = goal
    path = [current]
    while current != start:
        current = came_from[current]
        path.append(current)
    path.reverse()
    return path

came_from, miniCost = astar(graph, "Arad", "Bucharest")
print(reconstruct_path(came_from, "Arad", "Bucharest"))
print("The total cost needed: ", miniCost)


