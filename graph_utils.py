# graph_utils.py
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import os

# --- 1. Generate Random Graph (Erdős–Rényi Model) ---
def generate_random_graph(n=30, p=0.1):
    """
    Generate a random graph using the Erdős–Rényi model.
    n: number of nodes
    p: probability of an edge between any pair of nodes
    """
    G = nx.erdos_renyi_graph(n, p)
    return G

# --- 2. Generate Small-World Network (Watts–Strogatz Model) ---
def generate_small_world_graph(n=30, k=4, p=0.1):
    """
    Generate a small-world network using the Watts–Strogatz model.
    n: number of nodes
    k: number of nearest neighbors for each node
    p: rewiring probability
    """
    G = nx.watts_strogatz_graph(n, k, p)
    return G

# --- 3. Analyze Graph Properties ---
def analyze_graph(G):
    """
    Compute and print key graph metrics:
    - Number of nodes
    - Number of edges
    - Average clustering coefficient
    - Average path length
    """
    num_nodes = G.number_of_nodes()
    num_edges = G.number_of_edges()
    clustering = nx.average_clustering(G)

    try:
        path_length = nx.average_shortest_path_length(G)
    except nx.NetworkXError:
        path_length = None  # occurs if graph is disconnected

    analysis = {
        "nodes": num_nodes,
        "edges": num_edges,
        "avg_clustering": round(clustering, 3),
        "avg_path_length": round(path_length, 3) if path_length else "Not connected"
    }
    return analysis

# --- 4. Visualize Graph ---
def visualize_graph(G, title="Graph Visualization", filename=None):
    plt.figure(figsize=(6, 6))
    nx.draw(G, with_labels=True, node_color="skyblue", node_size=700, edge_color="gray")
    plt.title(title)
    if filename:
        os.makedirs("results", exist_ok=True)
        plt.savefig(f"results/{filename}")
    plt.show()

# --- 5. Analyze how properties change with rewiring probability ---
def small_world_analysis(n=50, k=4, steps=20):
    ps = np.linspace(0, 1, steps)
    clustering = []
    path_length = []

    for p in ps:
        G = nx.watts_strogatz_graph(n, k, p)
        clustering.append(nx.average_clustering(G))
        try:
            path_length.append(nx.average_shortest_path_length(G))
        except nx.NetworkXError:
            path_length.append(np.nan)

    plt.figure(figsize=(8, 5))
    plt.plot(ps, clustering, 'o-', label='Clustering Coefficient')
    plt.plot(ps, path_length, 's-', label='Average Path Length')
    plt.xlabel('Rewiring Probability (p)')
    plt.ylabel('Metric Value')
    plt.title('Small-World Network Analysis')
    plt.legend()
    plt.grid(True)
    os.makedirs("results", exist_ok=True)
    plt.savefig("results/small_world_analysis.png")
    plt.show()
