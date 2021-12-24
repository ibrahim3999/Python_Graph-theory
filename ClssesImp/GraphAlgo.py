import json
import sys
from typing import List
from queue import  PriorityQueue
from DiGraph import DiGraph
from NodeData import NodeData
from src.GraphAlgoInterface import GraphAlgoInterface
from src.GraphInterface import GraphInterface
import heapq as hq

class GraphAlgo(GraphAlgoInterface):

    def __init__(self, G: DiGraph) -> object:
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
    def TSP(self, node_lst: List[int]) -> (List[int], float):
        min_tsp = []
        nodes = self.get_graph().get_all_v()
        for nodeStart in nodes:
            for nodeForward in nodes:
                if (nodeStart != nodeForward):
                    min_tsp.append(self.shortest_path(nodeStart, nodeForward))
        lstOfLst = [list(ele) for ele in min_tsp]
        sortList = sorted(lstOfLst)
        for i in range(len(sortList)):
            if set(sorted(node_lst)).issubset(set(sorted(sortList[i][1]))):
                return sortList[i][1], sortList[i][0]

        return [], -1


    def shortest_path(self, id1: int, id2: int) -> (float, list):
        if self.get_graph().get_all_v().get(id1) is None or self.get_graph().get_all_v().get(id2) is None:
            return float('inf'), []
        self.Rrefsh()
        shortest_path = self.rec(id1, id2, self.dijkstra(self.get_graph().get_all_v().get(id1), self.get_graph().get_all_v().get(id2)))
        return self.get_graph().get_all_v().get(id2).get_dist(), shortest_path

    def shortest_path_dist(self, id1: int, id2: int) -> (float, list):
        if self.get_graph().get_all_v().get(id1) is None or self.get_graph().get_all_v().get(id2) is None:
            return float('inf'), []
        self.Rrefsh()
        shortest_path = self.rec(id1, id2, self.dijkstra(self.get_graph().get_all_v().get(id1), self.get_graph().get_all_v().get(id2)))
        return self.get_graph().get_all_v().get(id2).get_dist()

    def centerPoint(self) -> (int, float):
        MaxResults = {}
        MinKey=-1
        MinOfAll = float('inf')
        nodes = self.__G.get_all_v()
        for n in nodes:
            max = -1
            for n1 in nodes:
                if(n!=n1):
                    dist = self.shortest_path_dist(n,n1)
                    if(dist!=float('inf')):
                        if(max<dist):
                            max=dist
            MaxResults[n] = max

        for key,val in MaxResults.items():
            if(MaxResults.get(key)<MinOfAll):
                MinOfAll=MaxResults.get(key)
                MinKey=key

        return MinKey,MinOfAll

    def rec(self, src: int, dest: int, allPath: dict) -> list:
        if allPath.get(dest) is None:
            return []
        short = [dest]
        parent = allPath.get(dest)
        while parent != src:
            short.insert(0, parent)
            parent = allPath.get(parent)
        short.insert(0, src)
        return short

    def dijkstra(self, src: NodeData, dest: NodeData) -> dict:
        src.set_dist(0)
        src.set_visited(True)
        h: hq = []
        hq.heappush(h, (0, src))
        res= {}
        while len(h) > 0:
            n: NodeData = hq.heappop(h)[1]
            if n.get_key() == dest.get_key():
                break
            if not n.get_visited():
                n.set_visited(True)
            for i in self.get_graph().all_out_edges_of_node(n.get_key()):
                v: NodeData= self.get_graph().get_all_v().get(i)
                if not v.get_visited():
                    if v.get_dist() == -1 or n.get_dist() + self.get_graph().all_out_edges_of_node(n.get_key()).get(i) < v.get_dist():
                        v.set_dist(n.get_dist() + self.get_graph().all_out_edges_of_node(n.get_key()).get(i))
                        hq.heappush(h, (n.get_dist() + self.get_graph().all_out_edges_of_node(n.get_key()).get(i), v))
                        res[v.get_key()] = n.get_key()
        return res
    def Rrefsh(self):
        vertx: dict = self.get_graph().get_all_v()
        for n in vertx:
            vertx.get(n).set_visited(False)
            vertx.get(n).set_dist(float('inf'))
if __name__ == '__main__':
    b=GraphAlgo(DiGraph())
    b.load_from_json(r"C:\Users\User\Desktop\Ex3\data\A0.json")
    ##print(b.get_graph().all_out_edges_of_node(0))
    ##    x = "C:\\Users\\User\\Desktop\\Ex3\\data\\y.json"
    ## b.save_to_json(x)
   ## print(b.getMax())
   ## print(b.centerPoint())
    print(b.centerPoint())
    print(b.TSP([0,1,3]))

