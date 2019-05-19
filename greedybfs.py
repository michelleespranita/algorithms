# graph = {"Linz": {"Self": 318, "Passau": 102, "Salzburg": 126}, "Passau": {"Self": 257, "Linz": 102, "Muenchen": 189},
#         "Salzburg": {"Self": 236, "Linz": 126, "Rosenheim": 81}, "Rosenheim": {"Self": 168, "Salzburg": 81, "Muenchen": 59},
#         "Muenchen": {"Self": 120, "Ulm": 123, "Memmingen": 115, "Passau": 189, "Rosenheim": 59},
#         "Ulm": {"Self": 0, "Memmingen": 55, "Muenchen": 123}, "Memmingen": {"Self": 47, "Ulm": 55, "Muenchen": 115}}

graph = {"Arad": {"Self": 366, "Zerind": 75, "Timisoara": 118, "Sibiu": 140}, "Zerind": {"Self": 374, "Arad": 75, "Oradea": 71}, "Timisoara": {"Self": 329, "Arad": 118, "Lugoj": 111},
        "Oradea": {"Self": 380, "Zerind": 71, "Sibiu": 151}, "Lugoj": {"Self": 244, "Timisoara": 111, "Mehadia": 70}, "Sibiu": {"Self": 253, "Oradea": 151, "Arad": 140, "Fagaras": 99, "Rimnicu": 80},
        "Mehadia": {"Self": 241, "Lugoj": 70, "Dobreta": 75}, "Dobreta": {"Self": 242, "Mehadia": 75, "Craiova": 120}, "Rimnicu": {"Self": 193, "Sibiu": 80, "Pitesti": 97, "Craiova": 146},
        "Fagaras": {"Self": 176, "Sibiu": 99, "Bucharest": 211}, "Pitesti": {"Self": 100, "Rimnicu": 97, "Craiova": 138, "Bucharest": 101}, "Bucharest": {"Self": 0, "Pitesti": 101, "Fagaras": 211, "Giurgiu": 90, "Urziceni": 85},
        "Giurgiu": {"Self": 77, "Bucharest": 90}, "Urziceni": {"Self": 80, "Bucharest": 85, "Hirsova": 98, "Vaslui": 142}, "Hirsova": {"Self": 151, "Urziceni": 98, "Eforie": 86}, "Eforie": {"Self": 161, "Hirsova": 86},
        "Vaslui": {"Self": 199, "Iasi": 92, "Urziceni": 142}, "Iasi": {"Self": 226, "Vaslui": 92, "Neamt": 87}, "Neamt": {"Self": 234, "Iasi": 87},
        "Craiova": {"Self": 160, "Dobreta": 120, "Rimnicu": 146, "Pitesti": 138}}

def greedySearch(graph, start, goal):
    graphWhole = graph
    path = [start]
    while start != goal:
        graph = graphWhole[start]
        cities = []
        citiesSLD = {}
        for city in graph.keys():
            if city != "Self":
                cities.append(city)
                
        for city in cities:
            citySLD = (graphWhole[city])["Self"]
            citiesSLD.update({city: citySLD})
            miniSLD = citySLD
            # print(miniSLD)

        # print(citiesSLD)

        for city, citySLD in citiesSLD.items():
            if miniSLD >= citySLD:
                miniSLD = citySLD
                miniCity = city
        start = miniCity
        path.append(start)

    return path

print(greedySearch(graph, "Arad", "Bucharest"))
