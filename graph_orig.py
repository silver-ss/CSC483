"""
Graph data structure supporting both adjacency matrix and adjacency list representations.

This module provides a Graph class that allows:
- Adding weighted edges to an adjacency matrix
- Displaying the adjacency matrix
- Adding weighted edges to an adjacency list
- Displaying the adjacency list

Users can create a graph with a specified number of vertices,
add edges between vertices, and inspect both underlying representations.
"""

from typing import Dict, List, Tuple


class Graph:
    """
    Graph that maintains both adjacency matrix and adjacency list.

    Provides methods to add undirected, weighted edges and to display
    each representation of the graph.
    """

    def __init__(self, num_vertices: int) -> None:
        """
        Initialize a graph with a provided number of vertices.

        Creates an empty adjacency matrix filled with zeros and an empty
        adjacency list mapping each vertex to a list of (neighbor, weight).

        Args:
            num_vertices (int): How many vertices the graph contains.

        Returns:
            None
        """
        self.num_vertices = num_vertices
        # Initialize adjacency matrix (num_vertices x num_vertices)
        self.adj_matrix: List[List[float]] = [
            [0.0 for _ in range(num_vertices)]
            for _ in range(num_vertices)
        ]
        # Initialize adjacency list {vertex: [(neighbor, weight), ...]}
        self.adj_list: Dict[int, List[Tuple[int, float]]] = {
            i: [] for i in range(num_vertices)
        }

    def add_edge_matrix(self, u: int, v: int, weight: float = 1.0) -> None:
        """
        Add an undirected, weighted edge between vertices u and v in the adjacency matrix.

        Updates both [u][v] and [v][u] entries to the specified weight.

        Args:
            u (int): Index of the first vertex.
            v (int): Index of the second vertex.
            weight (float, optional): Weight of the edge. Defaults to 1.0.

        Raises:
            IndexError: If either u or v is outside the valid vertex range.

        Returns:
            None
        """
        if (0 >= u > self.num_vertices) and (0 >= v > self.num_vertices):
            raise IndexError("Vertex index out of bounds")
        self.adj_matrix[u][v] = weight


    def display_matrix(self) -> None:
        """
        Print the adjacency matrix of the graph, one row per vertex.

        Returns:
            None
        """
        print("Adjacency Matrix:")
        for row in self.adj_matrix:
            print(row)

    def add_edge_list(self, u: int, v: int, weight: float = 1.0) -> None:
        """
        Add an undirected, weighted edge between vertices u and v in the adjacency list.

        Appends (v, weight) to u's neighbor list and (u, weight) to v's neighbor list.

        Args:
            u (int): Index of the first vertex.
            v (int): Index of the second vertex.
            weight (float, optional): Weight of the edge. Defaults to 1.0.

        Raises:
            IndexError: If either u or v is outside the valid vertex range.

        Returns:
            None
        """
        if u not in self.adj_list or v not in self.adj_list:
            raise IndexError("Vertex index out of bounds")
        self.adj_list[u].append((v, weight))
        self.adj_list[v].append((u, weight)) 

    def display_list(self) -> None:
        """
        Print the adjacency list of the graph, one vertex per line.

        Returns:
            None
        """
        print("Adjacency List:")
        for vertex, neighbors in self.adj_list.items():
            print(f"{vertex}: {neighbors}")


if __name__ == "__main__":
    # Create a graph with 4 vertices
    g = Graph(4)

    # Create weighted edges as (u, v, weight)
    edges = [
        (0, 1, 10.0),
        (0, 2, 5.0),
        (1, 2, 3.0),
        (2, 3, 1.0),
    ]

    # Add each edge to both the matrix and list representations
    for u, v, w in edges:
        g.add_edge_matrix(u, v, w)
        g.add_edge_list(u, v, w)

    # Display both representations
    g.display_matrix()
    print()
    g.display_list()