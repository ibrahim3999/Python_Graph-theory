import copy
import math
from typing import List
import json
from src.GraphAlgoInterface import GraphAlgoInterface
from src import GraphInterface
import matplotlib.pyplot as plt
import json
from queue import PriorityQueue
import math
from typing import List
from .DiGraph import DiGraph
from GraphAlgoInterface import GraphAlgoInterface
from GraphFrame import GraphFrame
from src.GraphInterface import GraphInterface


class GraphAlgo(GraphAlgoInterface):
    def plot_graph(self) -> None:
        pass

    def save_to_json(self, file_name: str) -> bool:
        pass

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        pass

    def load_from_json(self, file_name: str) -> bool:
        pass