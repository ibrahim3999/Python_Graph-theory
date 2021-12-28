import matplotlib.pyplot as plot_graph

from ClssesImp import NodeData
from DiGraph import DiGraph
import random


class GraphFrame:

    def __init__(self, graph: DiGraph):
        """

        """
        self.graph = graph
        self.draw_graph()

    def set_random_nodes(self):
        list_random_location_nodes = []
        for node in self.graph.get_all_v().values():
            if node.get_location() is None:
                list_random_location_nodes.append(node)
        if list_random_location_nodes.__len__() == 0:
            return
        for node in list_random_location_nodes: 
            if node.get_location() is None:
                node.set_location(random.uniform(0, 7), random.uniform(0, 7), 0)

    def draw_nodes(self, ax):
        self.set_random_nodes()
        nodes = self.graph.get_all_v()
        keys = []

        for node in self.graph.Nodes.values():
            key = node.get_key()
            keys.append(key)
            ax.scatter(node.get_location()[0], node.get_location()[1], color="blue",
                       label="Nodes", )  # Drawing the vertices using the position
        for i, txt in enumerate(keys):
            ax.annotate(keys[i], (nodes.get(keys[i]).get_location()[0], nodes.get(keys[i]).get_location()[1]),
                        color='r')  # Drawing the keys of the vertices

    def draw_edges(self, ax):
        eps = 0.0001
        x_lim = ax.get_xlim()[1] - ax.get_xlim()[0]
        y_lim = ax.get_ylim()[1] - ax.get_ylim()[0]
        node: NodeData = None
        for node in self.graph.Nodes.values():
            for edge in self.graph.all_out_edges_of_node(node.get_key()).keys():
                x1 = float(node.get_location()[0])
                x2 = float(self.graph.get_Node(edge).get_location()[0])
                y1 = float(node.get_location()[1])
                y2 = float(self.graph.get_Node(edge).get_location()[1])
                dx = abs(x1 - x2)
                dy = abs(y1 - y2)
                ax.arrow(x1, y1,
                         dx,
                         dy, label='Edges',
                         length_includes_head=True, width=0.00000389, head_width=x_lim * 0.007999,
                         head_length=y_lim * 0.01999)

    def draw_graph(self):
        plot_graph.figure(figsize=(11, 6), facecolor="#5a7d9a")
        ax = plot_graph.axes()
        plot_graph.title("Here is a graphic presentation of the graph:", color="w")
        plot_graph.xlabel("x")
        plot_graph.ylabel("y")
        self.draw_nodes(ax)
        self.draw_edges(ax)
        plot_graph.tight_layout()
        plot_graph.show()
