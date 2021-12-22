class NodeData:
    def __init__(self, key: int, tag=0, pos: tuple = None):
        self.__key: int = key
        self.__tag = tag
        self.__info = "none"
        self.__parent = None
        self.__location = pos

    def get_location(self) -> [tuple]:
        return self.__location

    def set_location(self, x, y, z):
        self.__location = (x, y, z)

    def get_key(self) -> int:
        return self.__key

    def set_key(self, key: int):
        self.__key = key

    def get_tag(self) -> float:
        return self.__tag

    def set_tag(self, tag: int):
        self.__tag = tag

    def get_parent(self) -> int:
        return self.__parent

    def set_parent(self, parent):
        self.__parent = parent

    def get_info(self) -> str:
        return self.__info

    def set_info(self, info: str):
        self.__info = info

    def __repr__(self):
        if self.__location is None:
            return '{ID:' + self.__key.__str__() + '}'
        else:
            return '{ID:' + self.__key.__str__() + ', Location:' + self.__location.__str__() + '}'

    def __lt__(self, other):
        return self.__tag < other.__tag

    def __gt__(self, other):
        return self.__tag > other.__tag