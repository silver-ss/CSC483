"""
Shortest path algorithms for weighted graphs.

This module provides  shortest path implementations:

- dijkstra: algorithm for graphs with nonnegative edge weights.
- bellman_ford: algorithm that handles negative weights and detects negative cycles.
- get_shortest_path: Reconstructs a path string from the .pred_vertex links.
- reset_state: Resets all Vertex.distance and .pred_vertex for a fresh run.

Depends on:
    Graph and Vertex classes from graphs.py
"""

import time
from graph import Graph, Vertex
from functools import wraps

def time_execution(func):
    """
    Decorator that records the execution time of the decorated function.

    Args:
        func (callable): The function to wrap.

    Returns:
        callable: A wrapped version of `func` that allows calling 
        last_time to get execution time.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        """
        Inner wrapper that times a single call to `func`.
        """
        start = time.perf_counter() # start time
        results = func(*args, **kwargs) #store any returned values
        run_time = time.perf_counter() - start
        wrapper.last_time = run_time
        return results
    wrapper.last_time = None # reset before each new run
    return wrapper

@time_execution
def dijkstra(g: Graph, start_vertex: Vertex) -> None:
    """
    Find shortest paths on a graph with non negative weights
    using Dijkstra algorithm.

    This updates each Vertex in g.adj_list by setting:
      - v.distance    = shortest distance from start_vertex to v
      - v.pred_vertex = preceding vertex on that shortest path (or None)

    Args:
        g (Graph): Graph with g.adj_list: Dict[Vertex, List[(Vertex, float)]]
        start_vertex (Vertex): Source vertex; must be in g.adj_list

    Returns:
        None
    """
    unvisited_queue: List[Vertex] = list(g.adj_list)

    start_vertex.distance = 0

    # Find index of vertex with minimum distance
    while len(unvisited_queue) > 0:
        smallest_index = 0
        for i in range(1, len(unvisited_queue)):
            if unvisited_queue[i].distance < unvisited_queue[smallest_index].distance:
                smallest_index = i
        current_vertex = unvisited_queue.pop(smallest_index)
        # Relax Edges to lowest possible weight
        for adj_vertex, weight in g.adj_list[current_vertex]:
            alt_path_distance = current_vertex.distance + weight

            if alt_path_distance < adj_vertex.distance:
                adj_vertex.distance = alt_path_distance
                adj_vertex.pred_vertex = current_vertex 

@time_execution
def bellman_ford(g: Graph, start_vertex: Vertex) -> bool:
    """
    Compute shortest paths on a graph that may have
    negative weights and detect negative cycles.

    This updates each Vertex in g.adj_list by setting:
      - v.distance = shortest distance from start to v
      - v.pred_vertex = preceding vertex on that shortest path (or None)

    After len(g.adj_list) -1 passes of edge relaxation, one more pass checks
    for negative weight cycles. If any distance can still be decreased
    returns False to signal a negative cycle.

    Args:
        g (Graph): Graph with g.adj_list: Dict[Vertex, List[(Vertex, float)]]
        start (Vertex): Source vertex; must be in g.adj_list

    Returns:
        bool: True if no negative cycle detected, False otherwise
    """
    start_vertex.distance = 0

    #relax edges len(g.adj_list) - 1 times
    for _ in range(len(g.adj_list) - 1):
        for current_vertex in g.adj_list:
            for adj_vertex, weight in g.adj_list[current_vertex]:
                alt_path_distance = current_vertex.distance + weight
                if alt_path_distance < adj_vertex.distance:
                    adj_vertex.distance = alt_path_distance
                    adj_vertex.pred_vertex = current_vertex

    #check for negative weight cycle
    for current_vertex in g.adj_list:
        for adj_vertex, weight in g.adj_list[current_vertex]:
            alt_path_distance = current_vertex.distance + weight

            if alt_path_distance < adj_vertex.distance:
                return False #found negative weight cycle

    return True #does not contain negative weight cycle

def get_shortest_path(start: Vertex, end: Vertex) -> str:
    """
    Reconstruct the shortest path string from start to end
    using each vertex.pred_vertex chain.

    use after calling dijkstra() or bellman_ford()
    so that .distance and .pred_vertex are set.

    Args:
        start (Vertex):  Source vertex
        end (Vertex):  Target vertex

    Returns:
        str: A path like "a -> b -> c", or
             "a → d: no path exists" if end.distance is 'inf'.
    """
    if end.distance == float('inf'):
        return f"{start.label} → {end.label}: no path exists"

    parts = []
    current_vector = end
    while current_vector is not start:
        parts.append(current_vector.label)
        current_vector = current_vector.pred_vertex
    parts.append(start.label)
    parts.reverse()
    return " -> ".join(parts)

def reset_state(g: Graph):
    """
    Resets the distance and pred_vertex attributes for 
    all vertex in g.adj_list so next algo runs from a 
    clean slate

    Sets:
        - v.distance = 'inf'
        - v.pred_vertex = None
    for all vertex in g.adj_list

    Args:
        g: (Graph): the graph to reset vertex attributes for

    Returns:
        None
    """
    for v in g.adj_list:
        v.distance = float('inf')
        v.pred_vertex = None