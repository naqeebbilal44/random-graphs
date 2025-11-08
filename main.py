# main.py
from graph_utils import (
    generate_random_graph,
    generate_small_world_graph,
    analyze_graph,
    visualize_graph,
    small_world_analysis
)

def main():
    print("=== Random Graph Simulation ===")
    G_random = generate_random_graph(n=20, p=0.2)
    visualize_graph(G_random, "Random Graph (Erdős–Rényi)", "random_graph.png")
    print(analyze_graph(G_random))

    print("\n=== Small-World Network Simulation ===")
    G_small = generate_small_world_graph(n=30, k=4, p=0.3)
    visualize_graph(G_small, "Small-World Network (Watts–Strogatz)", "small_world.png")
    print(analyze_graph(G_small))

    print("\n=== Analyzing Small-World Properties for Different Rewiring Probabilities ===")
    small_world_analysis(n=50, k=4)

if __name__ == "__main__":
    main()
