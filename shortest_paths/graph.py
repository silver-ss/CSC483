"""
Graph data structure supporting adjacency list.

This module provides a Graph class that allows:
- Adding weighted edges to an adjacency list
- Displaying the adjacency list

Users can create a graph with a specified number of vertices,
add edges between vertices.
"""

from typing import Dict, List, Tuple

class Vertex:

    def __init__(self,label):
        self.label = label
        self.distance = float('inf')
        self.pred_vertex = None

class Graph:
    """
    Graph that maintains adjacency list.

    Provides methods to add undirected, weighted edges and to display
    the graph.
    """

    def __init__(self, directed: bool = False) -> None:
        """
        Initialize a graph with a provided number of vertices.

        Creates an empty adjacency list mapping each vertex to a list 
        of (neighbor, weight).

        Args:
            directed (bool): if True create directed graph

        Returns:
            None
        """
        self.edge_weights: Dict[Tuple[Vertex, Vertex], float] = {}
        # Initialize adjacency list {vertex: [(neighbor, weight), ...]}
        self.adj_list: Dict[Vertex, List[Tuple[Vertex, float]]] = {}
        self.directed = directed
    
    def add_vertex(self, v: Vertex):
        if v not in self.adj_list:
            self.adj_list[v] = []

       
    def add_edge_list(self, u: Vertex, v: Vertex, weight: float = 1.0) -> None:
        """
        Add an undirected, weighted edge between vertices u and v in the adjacency list.

        Appends (v, weight) to u's neighbor list and (u, weight) to v's neighbor list.

        Args:
            u (int): Index of the first vertex.
            v (int): Index of the second vertex.
            weight (float, optional): Weight of the edge. Defaults to 1.0.

        Returns:
            None
        """
        self.add_vertex(u)
        self.add_vertex(v)

        self.edge_weights[(u,v)] = weight        
        self.adj_list[u].append((v, weight))
         
        #if undirected graph add reverse edge
        if not self.directed:
            self.edge_weights[(v,u)] = weight
            self.adj_list[v].append((u, weight))
   
    def display_list(self) -> None:
        """
        Print the adjacency list of the graph, one vertex per line, showing
        each neighbor and the weight of the connecting edge.
        """
        print("Adjacency List:")
        for vertex, neighbors in self.adj_list.items():
            entries = ", ".join(f"{nbr.label}({w})" for nbr, w in neighbors)
            print(f"{vertex.label}: [{entries}]")

        print("\nEdge Weights:")
        for (u, v), w in self.edge_weights.items():
            print(f"{u.label} -> {v.label}: {w}")