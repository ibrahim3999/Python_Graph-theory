from NodeData import NodeData
from src.GraphInterface import GraphInterface


class DiGraph(GraphInterface):
    Nodes = dict()
    Edges_out = dict()
    Edges_in = dict()

    def __init__(self):
        super()
        self.Nodes = dict()
        self.Edges_out = dict()
        self.Edges_in = dict()
        self.Edges = dict(dict())
        self.__nodeSize = 0
        self.__edgeSize = 0
        self.__mc = 0

    def get_Node(self, i):
        return self.Nodes.get(i)

    def remove_edge(self, node_id1, node_id2):

        if node_id1 != node_id2 and node_id2 in self.Edges_out.get(node_id1):
            self.Edges_out.get(node_id1).pop(node_id2)
            self.Edges_in.get(node_id2).pop(node_id1)
            self.__edgeSize -= 1
            self.__mc += 1
            return True
        if node_id1 not in self.Nodes or node_id2 not in self.Nodes or node_id1 == node_id2:
            return False

    def remove_node(self, node_id):
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

    def add_node(self, node_id, pos=None):

        if node_id not in self.Nodes:
            self.Nodes[node_id] = NodeData(key=node_id, pos=pos)
            self.Edges_in.__setitem__(node_id, {})
            self.Edges_out.__setitem__(node_id, {})
            self.__nodeSize += 1
            self.__mc += 1
            return True
        return False

    def add_edge(self, id1, id2, weight):

        nodes = self.get_all_v().keys()
        if id1 != id2 and id1 in nodes and id2 in nodes and id2 not in self.Edges_out[id1] and weight >= 0:
            self.Edges_in[id2][id1] = weight
            self.Edges_out[id1][id2] = weight
            self.__mc += 1
            self.__edgeSize += 1
            return True
        return False

    def get_mc(self):
        return self.__mc

    def get_all_v(self):
        return self.Nodes

    def all_in_edges_of_node(self, id1):

        if id1 not in self.Nodes:
            return {}
        return self.Edges_in.get(id1)

    def all_out_edges_of_node(self, id1):

        if id1 not in self.Nodes:
            return {}
        return self.Edges_out.get(id1)

    def e_size(self):
        return self.__edgeSize

    def v_size(self):
        return len(self.Nodes)
