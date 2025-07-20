import operator
from typing import List, Tuple
from graph import Graph, Vertex
from shortest_paths import (
    dijkstra, bellman_ford, get_shortest_path, reset_state
)

a,b,c,d = Vertex('a'), Vertex('b'), Vertex('c'), Vertex('d')

def create_graph(
    edges: List[Tuple[Vertex, Vertex, float]],
    is_directed: bool = False
) -> Graph:
    """
    Build and return a Graph from a list of weighted edges.

    Args:
        edges: List of (u, v, weight) triples where u and v are Vertex objects.
        is_directed(bool): True if you want a directed graph

    Returns:
        Graph: A graph containing exactly those edges (and their endpoints).
    """
    g = Graph(is_directed)
    for u,v,w in edges:
        g.add_edge_list(u,v,w)
    return g

def dijkstra_vs_bellman(g, start_vertex):
    #bellman
    reset_state(g)
    no_negative_cycle = bellman_ford(g, start_vertex)
    b_run_time = bellman_ford.last_time
    status = "negative cycle detected" if not no_negative_cycle else "no negative cycle"
    print(f"\nBellman-Ford took {b_run_time} seconds ({status})")
    if no_negative_cycle:
        for v in sorted(g.adj_list, key=operator.attrgetter("label")):
            if v is not start_vertex and v.pred_vertex is None:
                print(f"{start_vertex.label} → {v.label}: no path exists")
            else:
                path = get_shortest_path(start_vertex, v)
                print(f"{start_vertex.label} → {v.label}: {path} (cost={v.distance})")
    if no_negative_cycle:
    # dijkstra
        reset_state(g)
        dijkstra(g, start_vertex)
        d_run_time = dijkstra.last_time
        print(f"\nDijkstra took {d_run_time} seconds")
        for v in sorted(g.adj_list, key=operator.attrgetter("label")):
            if v.pred_vertex is None and v is not start_vertex:
                 print(f"{start_vertex.label} → {v.label}: no path exists")
            else:
                path = get_shortest_path(start_vertex, v)
                print(f"{start_vertex.label} → {v.label}: {path} (cost={v.distance})")
    else: 
        print("Skipping Dijkstra, Negative Cycle found by Bellman-Ford")

    

if __name__ == "__main__":

    for x in range(100):
        if x == 10:
            print("running a few warmup laps...")

    # Graph A: all non-negative weights
    all_non_neg_edges = [
        (a, b, 10),
        (a, c, 5),
        (b, c, 3),
        (c, d, 1),
    ]
    print("=== Graph A (all non negative) ===")
    gA = create_graph(all_non_neg_edges)
    gA.display_list()
    dijkstra_vs_bellman(gA, a)


    # Graph B: contains a negative-weight cycle
    negative_cycle_edges = [
        (a, b, -10),
        (a, c, 5),
        (b, c, -3),
        (c, d, 1),
    ]
    print("\n=== Graph B (negative weight cycle) ===")
    gB = create_graph(negative_cycle_edges)
    gB.display_list()
    dijkstra_vs_bellman(gB, a)

    # Graph C: contains a negative edge, no negative cycle
    negative_edge = [
        (a, b, 10),
        (a, c, 5),
        (b, c, -6),
        (c, d, 1),
    ]
    print("\n=== Graph C (directed, negative edge) ===")
    gC = create_graph(negative_edge, True)
    gC.display_list()
    dijkstra_vs_bellman(gC, a)