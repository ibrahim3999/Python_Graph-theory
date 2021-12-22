from NodeData import NodeData
from src.GraphInterface import GraphInterface


class DiGraph(GraphInterface):

    def __init__(self):

        super()
        self.Nodes = dict()
        self.Edges_out = dict()
        self.Edges_in = dict()
        self.__nodeSize = 0
        self.__edgeSize = 0
        self.__mc = 0

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:

        if node_id1 != node_id2 and node_id2 in self.Edges_out.get(node_id1):
            self.Edges_out.get(node_id1).pop(node_id2)
            self.Edges_in.get(node_id2).pop(node_id1)
            self.__edgeSize -= 1
            self.__mc += 1
            return True
        if node_id1 not in self.Nodes or node_id2 not in self.Nodes or node_id1 == node_id2:
            return False

    def remove_node(self, node_id: int) -> bool:
        if node_id in self.Nodes:
            for edges in list(self.all_out_edges_of_node(node_id).keys()):
                self.remove_edge(node_id, edges)
            for edges in list(self.all_in_edges_of_node(node_id).keys()):
                self.remove_edge(edges, node_id)

            self.Nodes.pop(node_id)
            self.Edges_out.pop(node_id)
            self.Edges_in.pop(node_id)
            self.__nodeSize -= 1
            return True
        else:
            return False

    def add_node(self, node_id: int, pos: tuple = None) -> bool:

        if node_id not in self.Nodes:
            self.Nodes[node_id] = NodeData(key=node_id, pos=pos)
            self.Edges_in.__setitem__(node_id, {})
            self.Edges_out.__setitem__(node_id, {})
            self.__nodeSize += 1
            self.__mc += 1
            return True
        return False

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:

        nodes = self.get_all_v().keys()
        if id1 != id2 and id1 in nodes and id2 in nodes and id2 not in self.Edges_out[id1] and weight >= 0:
            self.Edges_in[id2][id1] = weight
            self.Edges_out[id1][id2] = weight
            self.__mc += 1
            self.__edgeSize += 1
            return True
        return False

    def get_mc(self) -> int:
        return self.__mc

    def get_all_v(self) -> dict:
        return self.Nodes

    def all_in_edges_of_node(self, id1: int) -> dict:

        if id1 not in self.Nodes:
            return {}
        return self.Edges_in.get(id1)

    def all_out_edges_of_node(self, id1: int) -> dict:

        if id1 not in self.Nodes:
            return {}
        return self.Edges_out.get(id1)

    def e_size(self) -> int:
        return self.__edgeSize

    def v_size(self) -> int:
        return len(self.Nodes)

    def __eq__(self, other):

        if type(other) is not DiGraph:
            return False
        if self.e_size() != DiGraph.e_size(other):
            return False
        if self.v_size() != DiGraph.e_size(other):
            return False
        for node in self.Nodes.values():
            if NodeData.get_key(node) not in DiGraph.get_all_v(other).keys():
                return False
            return True

    def __repr__(self):
        return f"Graph: |V|={self.v_size()} , |E|={self.e_size()}"
