import unittest
from ClssesImp.DiGraph import DiGraph


class TestDiGraph(unittest.TestCase):

    def build_graph(self):
        digraph = DiGraph()
        digraph.add_node(0)
        digraph.add_node(1)
        digraph.add_edge(0, 1, 1.5)
        digraph.add_node(2)
        digraph.add_edge(1, 2, 2)
        digraph.add_edge(2, 1, 1.1)
        digraph.add_node(3)
        digraph.add_edge(2, 3, 1.5)
        digraph.add_node(4)
        digraph.add_edge(3, 4, 2.5)
        digraph.add_edge(0, 4, 0.5)
        digraph.add_edge(4, 0, 0.5)
        return digraph

    def test_v_size(self):
        digraph = TestDiGraph.build_graph(self)
        number_nodes = digraph.v_size()
        self.assertEqual(5, number_nodes)
        digraph.add_node(5)
        self.assertEqual(6, digraph.v_size())
        digraph.remove_node(5)
        self.assertEqual(5, digraph.v_size())

    def test_e_size(self):
        digraph = TestDiGraph.build_graph(self)
        number_edges = digraph.e_size()
        self.assertEqual(7, number_edges)
        digraph.add_edge(3, 0, 7)
        self.assertEqual(8, digraph.e_size())
        digraph.remove_edge(1, 0)
        self.assertEqual(8, digraph.e_size())
        digraph.remove_edge(0, 1)
        self.assertEqual(7, digraph.e_size())

    def test_get_all_v(self):
        digraph = TestDiGraph.build_graph(self)
        nodes = digraph.get_all_v()
        number_nodes = digraph.v_size()
        for i in range(number_nodes):
            self.assertIn(i, nodes)
        self.assertEqual(5, nodes.__len__())
        digraph.add_node(5)
        self.assertTrue(5 in nodes)
        digraph.remove_node(5)
        self.assertFalse(5 in nodes)

    def test_all_in_edges_of_node(self):
        digraph = TestDiGraph.build_graph(self)
        self.assertIsNotNone(digraph.all_in_edges_of_node(0))
        self.assertIn(4, digraph.all_in_edges_of_node(0))
        digraph.remove_edge(4, 0)
        self.assertEqual({}, digraph.all_in_edges_of_node(0))
        self.assertIsNotNone(digraph.all_in_edges_of_node(1))
        self.assertIn(0, digraph.all_in_edges_of_node(1))
        self.assertIn(2, digraph.all_in_edges_of_node(1))
        self.assertEqual({}, digraph.all_in_edges_of_node(10))

    def test_get_mc(self):
        digraph = TestDiGraph.build_graph(self)
        mode_counter = digraph.get_mc()
        self.assertEqual(12, mode_counter)
        digraph.add_node(5)
        mode_counter = digraph.get_mc()
        self.assertEqual(13, mode_counter)
        digraph.remove_node(5)
        mode_counter = digraph.get_mc()
        digraph.remove_edge(0, 4)
        new_mode_counter = digraph.get_mc()
        self.assertNotEqual(mode_counter, new_mode_counter)
        mode_counter = digraph.get_mc()
        digraph.add_edge(0, 4, 10)
        new_mode_counter = digraph.get_mc()
        self.assertEqual(mode_counter + 1, new_mode_counter)
        digraph.add_edge(0, 4, 5)
        digraph.add_edge(0, 4, 8)
        digraph.add_node(2)
        digraph.add_node(3)
        self.assertEqual(new_mode_counter, digraph.get_mc())
        digraph.add_node(6)
        self.assertEqual(new_mode_counter+1, digraph.get_mc())

    def test_all_out_edges_of_node(self):
        digraph = TestDiGraph.build_graph(self)
        self.assertIsNotNone(digraph.all_out_edges_of_node(0))
        self.assertIn(1, digraph.all_out_edges_of_node(0))
        self.assertIn(4, digraph.all_out_edges_of_node(0))
        self.assertNotIn(3, digraph.all_out_edges_of_node(0))
        self.assertIsNotNone(digraph.all_out_edges_of_node(1))
        self.assertIn(2, digraph.all_out_edges_of_node(1))
        digraph.remove_edge(1, 2)
        self.assertNotIn(1, digraph.all_out_edges_of_node(1))
        self.assertEqual({}, digraph.all_out_edges_of_node(1))
        self.assertEqual({}, digraph.all_in_edges_of_node(10))

    def test_add_edge(self):
        digraph = TestDiGraph.build_graph(self)
        edges1 = digraph.e_size()
        digraph.add_edge(4, 3, 1)
        edges2 = digraph.e_size()
        self.assertEqual(edges2, edges1 + 1, "edges1 + 1 should equals edges2")
        weight = digraph.all_out_edges_of_node(4).get(3)
        self.assertEqual(1, weight, "weight should be 1")

    def test_add_node(self):
        digraph = TestDiGraph.build_graph(self)
        digraph.add_node(10)
        dict1 = digraph.get_all_v()
        self.assertIn(10, dict1)
        digraph.add_node(15)
        self.assertIn(15, dict1)
        self.assertNotIn(11, dict1)

    def test_remove_node(self):
        digraph = TestDiGraph.build_graph(self)
        digraph.remove_node(3)
        self.assertEqual(5, digraph.e_size())
        self.assertEqual(4, digraph.v_size())
        self.assertNotIn(3, digraph.get_all_v())
        self.assertIn(2, digraph.get_all_v())
        digraph.remove_node(2)
        self.assertEqual(3, digraph.e_size())
        self.assertEqual(3, digraph.v_size())
        self.assertNotIn(2, digraph.get_all_v())

    def test_remove_edge(self):
        digraph = TestDiGraph.build_graph(self)
        digraph.remove_edge(3, 4)
        self.assertEqual(6, digraph.e_size())
        self.assertEqual(0, len(digraph.all_out_edges_of_node(3)))
        self.assertEqual(2, len(digraph.all_out_edges_of_node(0)))
        digraph.remove_edge(0, 4)
        self.assertEqual(1, len(digraph.all_out_edges_of_node(0)))
        self.assertEqual(1, len(digraph.all_in_edges_of_node(0)))


if __name__ == '__main__':
    unittest.main()
