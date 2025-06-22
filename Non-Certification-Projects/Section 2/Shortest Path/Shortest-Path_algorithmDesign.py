# Define a weighted graph using adjacency lists
# Each node points to a list of (neighbor, distance) tuples
my_graph = {
    'A': [('B', 5), ('C', 3), ('E', 11)],
    'B': [('A', 5), ('C', 1), ('F', 2)],
    'C': [('A', 3), ('B', 1), ('D', 1), ('E', 5)],
    'D': [('C', 1), ('E', 9), ('F', 3)],
    'E': [('A', 11), ('C', 5), ('D', 9)],
    'F': [('B', 2), ('D', 3)]
}


def shortest_path(graph, start, target=''):
    """
    Implements Dijkstra's algorithm to compute the shortest path
    from a start node to all other nodes in a weighted graph.

    Args:
        graph (dict): The graph represented as an adjacency list.
        start (str): The starting node.
        target (str, optional): A specific target node to display. Defaults to ''.

    Returns:
        tuple: A dictionary of shortest distances and a dictionary of shortest paths.
    """

    unvisited = list(graph)  # Track all unvisited nodes
    # Initialize distances: 0 for start node, ∞ for all others
    distances = {node: 0 if node == start else float('inf') for node in graph}
    # Initialize paths: each node maps to an empty path list
    paths = {node: [] for node in graph}
    paths[start].append(start)  # Start node path begins with itself

    while unvisited:
        # Select the unvisited node with the smallest known distance
        current = min(unvisited, key=distances.get)

        # Examine all neighbors of the current node
        for node, distance in graph[current]:
            # Calculate new possible distance via current
            if distance + distances[current] < distances[node]:
                distances[node] = distance + distances[current]  # Update distance

                # Rebuild the shortest path to this neighbor
                if paths[node] and paths[node][-1] == node:
                    paths[node] = paths[current][:]
                else:
                    paths[node].extend(paths[current])
                paths[node].append(node)

        unvisited.remove(current)  # Mark current node as visited

    # Determine which nodes to display results for
    targets_to_print = [target] if target else graph
    for node in targets_to_print:
        if node == start:
            continue
        print(f'\n{start}-{node} distance: {distances[node]}\nPath: {" -> ".join(paths[node])}')

    return distances, paths


# Run the algorithm from node 'A', printing the path and distance to node 'F'


shortest_path(my_graph, 'A', 'B')  # Expected: A -> C -> B (distance: 4)
shortest_path(my_graph, 'A', 'C')  # Expected: A -> C (distance: 3)
shortest_path(my_graph, 'A', 'D')  # Expected: A -> C -> D (distance: 4)
shortest_path(my_graph, 'A', 'E')  # Expected: A -> C -> E (distance: 8)
shortest_path(my_graph, 'A', 'F')  # Expected: A -> C -> B -> F (distance: 6)