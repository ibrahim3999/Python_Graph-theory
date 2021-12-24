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
        try:
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
        except NameError:
            return False
        finally:
            f.close()

    def save_to_json(self, file_name: str) -> bool:
        if self.__G is None:
            return False
        ans = {"Edges": [], "Nodes": []}
        for i in self.__G.Nodes.values():
            nodeDict = {"id": i.get_key(), "pos": i.get_location()}
            ans["Nodes"].append(nodeDict)
            for j in self.__G.Edges_out.get(i.get_key()):
                Edges = {"src": i.get_key(), "w": self.__G.Edges_out.get(i.get_key())[j], "dest": j}
                ans["Edges"].append(Edges)
        try:
            with open(file_name, 'w') as W:
                W.write(json.dumps(ans))
                return True
        except NameError:
            return False
        finally:
            W.close()


    def shortest_path(self, id1: int, id2: int) -> (float, list):
        path = []
        nodes = self.graph.get_all_v()
        if id1 not in nodes or id2 not in nodes:
            return  math.inf, path
        if id1 == id2:
            path.append(id2)
            return 0, path
        self.reset(nodes)
        nodes = self.dijkstra(nodes, id1)
        dist = nodes[id2].get_tag()
        if dist == math.inf:
            return math.inf, path
        dest = id2
        while dest != -1:
            next_node = nodes[dest]
            dest = next_node.get_parent()
            path.insert(0, next_node.get_key())
        return dest, path
    def reset(self, nodes):
        for node in nodes.values():
            node.set_tag(math.inf)
            node.set_info("no")
            node.set_parent(None)

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
        GraphFrame().draw_graph()


    def dijkstra(self, Nodes: dict, id1: int) -> list:
            firstnode = Nodes[id1]
            firstnode.ClssesImp.NodeData.set_parent(-1)
            queue = PriorityQueue()
            queue.put(firstnode)
            firstnode
            while not (queue.empty()):
                vx = queue.get()
                EdgesOut = self.graph.all_out_edges_of_node(vx.get_key())
                for key, weight in edges_out.items():
                    if vx.ClssesImp.NodeData.get_tag() + weight < nodes[key].ClssesImp.NodeData.get_tag():
                        queue.put(nodes[key])
                        nodes[key].ClssesImp.NodeData.set_tag(vx.ClssesImp.NodeData.get_tag()+weight)
                        nodes[key].ClssesImp.NodeData.set_parent(vx.ClssesImp.NodeData.get_key())

            return nodes






    def __eq__(self, other):
        if type(other) is not GraphAlgo:
            return False
        if self.__G.__eq__(GraphAlgo.get_graph(other)):
            return True
        return False



if __name__ == '__main__':
    a = DiGraph()
    b = GraphAlgo(a)

    b.load_from_json(r"C:\Users\User\Desktop\Ex3\data\A0.json")
    nodes = b.get_graph().e_size()
    print(nodes)
    x = "C:\\Users\\User\\Desktop\\Ex3\\data\\y.json"
    b.save_to_json(x)
    print(a.Nodes.keys())
