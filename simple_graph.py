class Graph(object):

    def __init__(self):
        self.graph == {}

    def nodes(self):
        pass

    def edges(self):
        pass

    def add_node(self, node):
        self.graph.setdefault(node, [])

    def add_edge(self, node1, node2):
        try:
            self.graph.setdefault(node2, [])
            self.graph[node1].append(node2)
        except KeyError:
            self.graph.setdefault(node1, [node2])

    def del_node(self, node):
        self.graph.pop(node, None)

    def del_edge(self, node1, node2):
        temp = ''
        try:
            temp = self.graph[node1]
        except KeyError:
            raise KeyError("{} does not exist".format(node1))
        try:
            temp.remove(node2)
        except KeyError:
            raise KeyError("{} does not exist".format(node2))

    def has_node(self, node):
        return node in self.graph

    def neighbors(self, node):
        try:
            return self.graph[node]
        except KeyError:
            raise KeyError("{} doesn't exist".format(node))

    def adjacent(self, node1, node2):
        try:
            return node2 in self.graph[node1]
        except KeyError:
            raise KeyError("{} doesn't exist".format(node1))




