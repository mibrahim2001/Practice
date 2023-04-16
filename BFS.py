graph = {
'A': {'B': 2, 'C': 5},
'B': {'A': 2, 'D': 3},
'C': {'A': 5, 'D': 2, 'E': 4},
'D': {'B': 3, 'C': 2, 'F': 1},
'E': {'C': 4, 'F': 3},
'F': {'D': 1, 'E': 3, 'G': 2},
'G': {'F': 2}

}


def bfs(graph, start):
    queue = [start]
    visited = set()
    visited.add(start)
    while queue:
        current = queue.pop(0)
        print(f"{current} ",end="")

        for neighbour in graph[current].keys():
            if neighbour not in visited:
                queue.append(neighbour)
                visited.add(neighbour)
    


bfs(graph, 'A')