import unittest
import math
from ClssesImp.DiGraph import DiGraph
from ClssesImp.GraphAlgo import GraphAlgo


class GraphAlgoTest(unittest.TestCase):

    def build_graph(self):
        graph = DiGraph()
        graph.add_node(0)
        graph.add_node(1)
        graph.add_edge(0, 1, 1.5)
        graph.add_node(2)
        graph.add_edge(1, 2, 2)
        graph.add_edge(2, 1, 1.6)
        graph.add_node(3)
        graph.add_edge(2, 3, 1.5)
        graph.add_node(4)
        graph.add_edge(3, 4, 2.5)
        graph.add_edge(0, 4, 0.5)
        graph.add_edge(4, 0, 0.5)
        graph.add_edge(1, 0, 5)
        return graph

    def build_empty_graph(self):
        graph = DiGraph()
        return graph

    def test_shortest_path(self):
        graph = self.build_graph()
        graph_a = GraphAlgo()
        GraphAlgo.__init__(graph_a, graph)

        path_len = graph_a.shortest_path(2, 4).__getitem__(0)
        path_list = graph_a.shortest_path(2, 4).__getitem__(1)
        expected_list = [2, 3, 4]
        self.assertEqual(4, path_len)
        self.assertEqual(3, len(path_list))
        self.assertEqual(expected_list.__str__(), path_list.__str__())

        path_len = graph_a.shortest_path(1, 4).__getitem__(0)
        path_list = graph_a.shortest_path(1, 4).__getitem__(1)
        expected_list = [1, 0, 4]
        self.assertEqual(5.5, path_len)
        self.assertEqual(3, len(path_list))
        self.assertEqual(expected_list.__str__(), path_list.__str__())

        graph = self.build_empty_graph()
        graph_a.__init__(graph)
        path_len = graph_a.shortest_path(1, 50).__getitem__(0)
        path_list = graph_a.shortest_path(1, 50).__getitem__(1)
        self.assertEqual(math.inf, path_len)
        self.assertEqual([], path_list)
if __name__ == '__main__':
    unittest.main()
