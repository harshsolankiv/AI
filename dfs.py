tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': []
}


def DFS(tree, start, end):
    stack = [[start]]
    visited = []
    while stack:
        path = stack.pop(0)
        node = path[-1]
        if node == end:
            return path
        for i in tree[node]:
            if i not in visited:
                newPath = path + [i]
                stack.insert(0, newPath)
                visited.append(i)


start = input("enter the start node: ")
end = input("enter the end node: ")

ans = DFS(tree, start, end)
print(f"path is: {ans}")
