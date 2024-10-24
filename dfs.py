# Function to implement DFS
def dfs(graph, start_node, visited=None):
    if visited is None:
        visited = set()
    
    # Mark the current node as visited
    visited.add(start_node)
    print(start_node, end=" ")

    # Recur for all the neighbors (adjacent nodes) of the current node
    for neighbor in graph[start_node]:
        print(neighbor)
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Function to build the graph dynamically
def build_graph():
    graph = {}
    
    # Number of nodes
    num_nodes = int(input("Enter the number of nodes: "))
    
    # Input nodes and their neighbors
    for _ in range(num_nodes):
        node = input("Enter the node: ")
        neighbors = input(f"Enter the neighbors of {node} separated by space: ").split()
        graph[node] = neighbors
    
    return graph

# Main function
if __name__ == "__main__":
    # Build the graph from user input
    graph = build_graph()
    
    # Input the starting node for DFS
    start_node = input("Enter the starting node for DFS: ")
    
    # Perform DFS traversal
    print("DFS traversal starting from", start_node, ":")
    dfs(graph, start_node)
