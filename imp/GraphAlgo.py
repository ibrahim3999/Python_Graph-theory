import json
from typing import List

from DiGraph import DiGraph
from src.GraphAlgoInterface import GraphAlgoInterface
from src.GraphInterface import GraphInterface


class GraphAlgo(GraphAlgoInterface):

    def __init__(self, G: DiGraph):
        self.__G = G

    def get_graph(self) -> GraphInterface:
        return self.__G

    def load_from_json(self, file_name: str) -> bool:
        with open(file_name, 'r') as f:
            j = json.load(f)
            Nodes = j['Nodes']
            Egdes = j['Edges']
        for i in Nodes:
            pos = i["pos"]
            self.__G.add_node(i["id"], pos)
        for j in Egdes:
            self.__G.add_edge(j["src"], j["dest"], j["w"])
        return True

        return False

    def save_to_json(self, file_name: str) -> bool:
        nodes = []
        edges = []
        for id in self.__G.Nodes.keys():
            nodes.append({"id": id, "pos": self.__G.Nodes.get(id)})
            for edge in self.__G.all_out_edges_of_node(id):
                edges.append({"src": id, "w": self.__G.Nodes.get(id), "dest": edge})

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        """
        Returns the shortest path from node id1 to node id2 using Dijkstra's Algorithm
        @param id1: The start node id
        @param id2: The end node id
        @return: The distance of the path, a list of the nodes ids that the path goes through
        Example:
#      >>> from GraphAlgo import GraphAlgo
#       >>> g_algo = GraphAlgo()
#        >>> g_algo.addNode(0)
#        >>> g_algo.addNode(1)
#        >>> g_algo.addNode(2)
#        >>> g_algo.addEdge(0,1,1)
#        >>> g_algo.addEdge(1,2,4)
#        >>> g_algo.shortestPath(0,1)
#        (1, [0, 1])
#        >>> g_algo.shortestPath(0,2)
#        (5, [0, 1, 2])
        Notes:
        If there is no path between id1 and id2, or one of them dose not exist the function returns (float('inf'),[])
        More info:
        https://en.wikipedia.org/wiki/Dijkstra's_algorithm
        """

    def TSP(self, node_lst: List[int]) -> (List[int], float):
        """
        Finds the shortest path that visits all the nodes in the list
        :param node_lst: A list of nodes id's
        :return: A list of the nodes id's in the path, and the overall distance
        """

    def centerPoint(self) -> (int, float):
        """
        Finds the node that has the shortest distance to it's farthest node.
        :return: The nodes id, min-maximum distance
        """

    def plot_graph(self) -> None:
        """
        Plots the graph.
        If the nodes have a position, the nodes will be placed there.
        Otherwise, they will be placed in a random but elegant manner.
        @return: None
        """


if __name__ == '__main__':
    a = DiGraph()
    b = GraphAlgo(a)

    b.load_from_json(r"C:\Users\User\Desktop\Ex3\data\A0.json")
    nodes = b.get_graph().e_size()
    print(nodes)
