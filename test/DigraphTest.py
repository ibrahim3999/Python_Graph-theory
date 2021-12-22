import unittest
from ClssesImp.DiGraph import DiGraph


class DigraphTest(unittest.TestCase):

    def Graphbuilder(self):

        diGraph = DiGraph()
        diGraph.add_node(0)
        diGraph.add_node(1)
        diGraph.add_node(2)
        diGraph.add_node(3)
        diGraph.add_node(4)
        diGraph.add_edge(0, 1, 1.5)
        diGraph.add_edge(1, 2, 2)
        diGraph.add_edge(2, 1, 1.1)
        diGraph.add_edge(2, 3, 1.5)
        diGraph.add_edge(3, 4, 2.5)
        diGraph.add_edge(0, 4, 0.5)
        diGraph.add_edge(4, 0, 0.5)
        return diGraph

    def v_size_tets(self):
        diGraph = DigraphTest.Graphbuilder(self)
        nodesize = diGraph.v_size()
        self.assertEqual(5, nodesize)

if __name__ == '__main__':
    unittest.main()
