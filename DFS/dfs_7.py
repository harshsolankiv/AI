visited = set()


def dfs(visited, graph, root):
    if root not in visited:
        print(root)
        visited.add(root)
        for neighbour in graph[root]:
            dfs(visited, graph, neighbour)


if __name__ == '__main__':
    # IF GRAPH NEED TO BE TAKEN AS INPUT
    n = int(input("enter the number of node: "))
    i = 0
    tree = dict()
    while(i < n):
        child = list()
        n1 = input(f"enter the value of node {i+1}: ")
        ch = input(f"Do you want to add child nodes for {n1} Y/N : ")
        if ch == 'Y':
            nc = int(input(f"enter the number of child nodes: "))
            J = 0
            while(J < nc):
                x = (input(f"enter the value of node: "))
                child.append(x)
                J += 1
        tree.update({n1: child})
        i += 1
    for k, v in tree.items():
        print(f'{k} ---> {v}')

    # IF GRAPH IS GIVEN
    # tree = {
    #     'A': ['B', 'C', 'D'],
    #     'B': ['E'],
    #     'C': ['D', 'E'],
    #     'D': [],
    #     'E': []
    # }
    start = input("enter the start node: ")
    print("DFS for given Graph is : ")
    dfs(visited, tree, start)
