from collections import deque

# Function to implement BFS
def bfs(graph, start_node):
    # Create a queue for BFS and enqueue the start node
    queue = deque([start_node])
    print(queue)
    
    # Set to keep track of visited nodes
    visited = set([start_node])
    print(visited)
    
    # Loop until the queue is empty
    while queue:
        # Dequeue a node from the front of the queue
        node = queue.popleft()
        print(node, end=" ")
        
        # Get all adjacent nodes (neighbors) of the dequeued node
        for neighbor in graph[node]:
            if neighbor not in visited:
                # Enqueue the unvisited neighbors
                queue.append(neighbor)
                visited.add(neighbor)

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
    
    # Input the starting node for BFS
    start_node = input("Enter the starting node for BFS: ")
    
    # Perform BFS traversal
    print("BFS traversal starting from", start_node, ":")
    bfs(graph, start_node)
