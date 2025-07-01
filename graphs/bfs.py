def bfs_iterative(graph,start):
    visited=set()
    queue=[start]
    while queue:
        node=queue.pop(0)
        if node not in visited:
            print(node)
            visited.add(node)
            if node in graph:
              queue.extend(graph[node])
graph={
    'A':['B','C'],
    'B':['D'],
    'C':['E'],
    'D':[],
    'E':[]
}
bfs_iterative(graph,'A')