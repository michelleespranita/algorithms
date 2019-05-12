class Graph:
    def __init__(self, numvertex):
        self.numvertex=numvertex
        self.adjMatrix=[[-1]*numvertex for i in range(numvertex)]
        self.vertices={}
        self.verticeslist=[0]*numvertex
    def set_vertex(self, vtx, id):
        if 0<=vtx<=self.numvertex:
            self.vertices[id]=vtx
            self.verticeslist[vtx]=id
    def set_edge(self, frm, to, cost=0):
        frm = self.vertices[frm]
        to = self.vertices[to]
        self.adjMatrix[frm][to]=cost
        self.adjMatrix[to][frm]=cost
    def get_vertex(self):
        return self.verticeslist
    def get_edge(self):
        edges=[]
        for i in range(self.numvertex):
            for j in range(self.numvertex):
                if(self.adjMatrix[i][j]!=-1):
                    edges.append((self.verticeslist[i], self.verticeslist[j], self.adjMatrix[i][j]))
        return edges
    def get_matrix(self):
        return self.adjMatrix

def ucs(graph, start, goal):
    visitedNodes = [start]
    expand = graph.vertices[start]
    activeEdges = {}
    path = []
    finalPath = [goal]
    totalCost = 0
    while goal not in visitedNodes:
        for i in range(graph.numvertex):
            if(graph.adjMatrix[expand][i]!=-1) and graph.verticeslist[i] not in visitedNodes:
#                 visitedNodes.append(graph.verticeslist[i])
                if expand != graph.vertices[start]:
                    activeEdges[(graph.verticeslist[expand], graph.verticeslist[i])] = graph.adjMatrix[expand][i] + graph.adjMatrix[expandBefore][expand]
                else:
                    activeEdges[(graph.verticeslist[expand], graph.verticeslist[i])] = graph.adjMatrix[expand][i]
        
        print("Visited nodes:", visitedNodes)
        print("Active edges:", activeEdges)
        
        for cost in activeEdges.values():
            minCost = cost
            
        for cost in activeEdges.values(): #Find the minimum cost of the edges
            if minCost > cost:
                minCost = cost
                
        print("Min Cost:", minCost)
        
        for coor, cost in activeEdges.items():
            if cost == minCost:
                path.append(coor)
                print("Path:", path)
                totalCost += minCost
                expandBefore = graph.vertices[coor[0]]
                expand = graph.vertices[coor[1]]
                print("Expand:", coor[1])
                visitedNodes.append(graph.verticeslist[expand])
                del activeEdges[coor]
                totalCost = cost
                break
        
    target = goal
    while target!=start:
        for coor in path:
            if coor[1]==target:
                target = coor[0]
                finalPath.append(target)
    return finalPath, totalCost
                
            

print("FIRST GRAPH")
graph = Graph(7)
graph.set_vertex(0,'a')
graph.set_vertex(1,'b')
graph.set_vertex(2,'c')
graph.set_vertex(3,'d')
graph.set_vertex(4,'e')
graph.set_vertex(5,'f')
graph.set_vertex(6,'g')
graph.set_edge('a','b',1)
graph.set_edge('a','c',2)
graph.set_edge('b','d',2)
graph.set_edge('b','e',1)
graph.set_edge('c','f',3)
graph.set_edge('c','g',1)
print(graph.get_vertex())
print(graph.get_edge())
print(graph.get_matrix())
finalPath, totalCost = ucs(graph, 'a', 'g')
print("Final path starting from the goal to start:", finalPath)
print("Total cost: ", totalCost)

# print("SECOND GRAPH")
# graph2 = Graph(10)
# graph2.set_vertex(0,'s')
# graph2.set_vertex(1,'a')
# graph2.set_vertex(2,'b')
# graph2.set_vertex(3,'c')
# graph2.set_vertex(4,'d')
# graph2.set_vertex(5,'e')
# graph2.set_vertex(6,'f')
# graph2.set_vertex(7,'g1')
# graph2.set_vertex(8,'g2')
# graph2.set_vertex(9,'g3')
# graph2.set_edge('s','a',5)
# graph2.set_edge('s','b',9)
# graph2.set_edge('s','d',6)
# graph2.set_edge('a','b',3)
# graph2.set_edge('a','g1',9)
# graph2.set_edge('b','a',2)
# graph2.set_edge('b','c',1)
# graph2.set_edge('c','s',6)
# graph2.set_edge('c','g2',5)
# graph2.set_edge('c','f',7)
# graph2.set_edge('d','s',1)
# graph2.set_edge('d','c',2)
# graph2.set_edge('d','e',2)
# graph2.set_edge('e','g3',7)
# graph2.set_edge('f','d',2)
# graph2.set_edge('f','g3',8)
# print(graph2.get_vertex())
# print(graph2.get_edge())
# print(graph2.get_matrix())
# finalPath, totalCost = ucs(graph2, 'a', 'g')
# print("Final path starting from the goal to start:", finalPath)
# print("Total cost: ", totalCost)