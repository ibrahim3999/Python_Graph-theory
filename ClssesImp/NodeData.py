import sys


class NodeData:
    def __init__(self, key, pos:tuple):
        self.__key = key
        self.__tag = 0
        self.__info = "none"
        self.__parent = None
        self.pos = pos
        self.__location = pos.split(",")
        self.__visited = False
        self.__dist = float('inf')
        self.__weight = 0
        self.distance = float('inf')

    def get_dist(self):
        return self.__dist

    def set_dist(self, d):
        self.__dist = d

    def get_visited(self):
        return self.__visited

    def set_visited(self, v):
        if v == 1:
            self.__visited = True
        else:
            self.__visited = False

    def get_location(self):
        res = []
        for i in self.__location:
            x: float = i
            res.append(i)
        return res

    def set_location(self, x, y, z):
        self.__location = (x, y, z)

    def get_key(self):
        return self.__key

    def set_key(self, key):
        self.__key = key

    def get_tag(self):
        return self.__tag

    def set_tag(self, tag):
        self.__tag = tag

    def get_parent(self):
        return self.__parent

    def set_parent(self, parent):
        self.__parent = parent

    def get_info(self):
        return self.__info

    def set_info(self, info):
        self.__info = info

    def get_weight(self):
        return self.weight

    def set_weight(self, w):
        self.__weight = w;

    def get_distance(self):
        return self.distance

    def set_distance(self, d):
        self.distance = d

    def __repr__(self):
        if self.__location is None:
            return '{ID:' + self.__key.__str__() + '}'
        else:
            return '{ID:' + self.__key.__str__() + ', Location:' + self.__location.__str__() + '}'

    def __lt__(self, other):
        return self.__tag < other.__tag

    def __gt__(self, other):
        return self.__tag > other.__tag
