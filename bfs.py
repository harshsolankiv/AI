def BFS(graph, start, dest):
    queue = list()
    visited = list()
    queue.append(start)
    result = list()
    while queue:
        node = queue.pop(0)
        visited.append(node)
        if node == dest:
            break
        for child in graph[node]:
            if child not in visited:
                queue.append(child)
    result = visited
    return result


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': []
}
start = input("enter the start node: ")
end = input("enter the end node: ")

ans = BFS(graph, start, end)
print(f"path is: {ans}")
