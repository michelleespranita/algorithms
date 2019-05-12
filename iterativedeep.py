def ids(graph, root, goal, limit):
    for i in range(limit+1):
        depth = dfs(graph, root, goal, i)
        if depth != None:
            print("Node", goal, "found at depth", depth)
            break
        else:
            print("Node not found but limit reached")

def dfs(graph, root, goal, limit): #return None if limit reached and nothing found, return depth if found
    seen = [root]
    stack = [root]
    popped = []
    depth = 0
    while stack:
        print("Stack: ", stack)
        expand = stack.pop() #pops from the end of the list
        popped.append(expand)
        print("Expand: ", expand)
        print("Depth: ", depth)
        print("Popped: ", popped)
        if depth <= limit: #If limit is still OK
            if expand == goal:
                return depth
            else:
                if graph[expand] and depth==limit: #Case 1: Expanded node still has kids but has reached limit
                    if stack: #If the expanded node still has friends at the same depth
                        print("Limit reached, retrying friend at same depth...")
                    else: #If all his friends have been checked or if he has no other friends at the same depth
                        return None

                elif graph[expand] and depth<limit: #Case 2: Expanded node still has kids and hasn't reached limit
                    for node in graph[expand]:
                        if node not in seen:
                            seen.append(node)
                            stack.append(node)
                    depth += 1

                else: #Case 3 and 4: The expanded node doesn't have any kids (may or may not have reached limit)
                #In this case, we have to check if the expanded node's parent and ALL his friends are in popped

                    for aKey, aValue in graph.items():
                        if expand in aValue:
                            parent = aKey
                    check = []
                    true = 0
                    for j in graph[parent]:
                        if j in popped:
                            check.append(j)
                    for j in graph[parent]:
                        if j in check:
                            true+=1
                    if true==len(graph[parent]): #If yes, it means that they have all been checked, so it's time to go back up the tree (depth-=1)
                        print("Limit reached, going back up...")
                        depth-=1
                    else: #If not, try checking his friends from the same depth
                        print("Limit reached, retrying friend...")
                        depth=depth
        else: #If we have reached the limit (This code is supposedly never gonna be executed because there are preventative measures above to ensure that depth is not increased when limit has been reached)
            print("Limit reached, retrying...")
            return None

graph = {1: [2,3], 2: [4,5], 3: [5,6,7,8], 4: [], 5: [], 6: [], 7: [], 8: [9,10], 9: [], 10: []}
graph2 = {'A': ['B', 'C'], 'B': ['D', 'E'], 'C': ['F', 'G'], 'D': [], 'E': ['H', 'I'], 'F': [], 'G': []}
print("FIRST GRAPH")
ids(graph, 1, 4, 2)
print("\nSECOND GRAPH")
ids(graph2, 'A', 'G', 2)
