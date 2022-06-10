# Insert node in undirected/directred and weighted/unweighted graph using adjacency List method
def add_node(v):
    if v in graph:
        print(v,"is present in graph.")
    else:
        graph[v] = []

graph = {}
add_node("A")
add_node("B")
add_node("C")
add_node("A")
print(graph)