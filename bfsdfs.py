import collections

def bfs(graph, root, goal):
    seen = set([root])
    queue = collections.deque([root])
    while queue:
        print("Queue: ", queue)
        expand = queue.popleft() #If I used .pop(), it would make no difference between using a stack and queue because it would pop from the right side of the deque (last item on the list)
        print("Expand: ", expand)
        if expand == goal:
            break
        else:
            for node in graph[expand]:
                if node not in seen:
                    seen.add(node)
                    queue.append(node)

def dfs(graph, root, goal):
    seen = set([root])
    stack = [root]
    while stack:
        print("Stack: ", stack)
        expand = stack.pop() #pops from the end of the list
        print("Expand: ", expand)
        if expand == goal:
            break
        else:
            for node in graph[expand]:
                if node not in seen:
                    seen.add(node)
                    stack.append(node)

graph = {1: [2,3], 2: [4,5], 3: [6,7,8], 4: [], 5: [], 6: [], 7: [], 8: []}
bfs(graph,1,5)
print("") #new line
dfs(graph,1,5)
