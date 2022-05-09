
path = list()


def DFS(currentNode, destination, graph, maxDepth, curList):
    print("Checking for destination", currentNode)
    curList.append(currentNode)
    if currentNode == destination:
        path.append(curList)
        return True
    if maxDepth <= 0:
        return False
    else:
        for node in graph[currentNode]:
            if DFS(node, destination, graph, maxDepth-1, curList):
                return True
            else:
                curList.pop()
        return False


def iterativeDDFS(currentNode, destination, graph, maxDepth):
    for i in range(maxDepth):
        curList = list()
        if DFS(currentNode, destination, graph, i, curList):
            return True
    return False


if __name__ == '__main__':
    tree = {
        'S': ['A', 'B'],
        'A': ['C', 'D'],
        'B': ['E', 'F'],
        'C': ['G'],
        'D': [],
        'E': ['H'],
        'F': [],
    }
    for k, v in tree.items():
        print(f'{k} ---> {v}')
    start = input("enter the start node: ")
    end = input("enter the end node: ")
    depth = int(input("Enter depth: "))
    if not iterativeDDFS(start, end, tree, depth):
        print("Path is not available")
    else:
        print("path exists")
        print(path.pop())
