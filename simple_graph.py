class Graph(object):

    def __init__(self):
        self.graph = {}

    def nodes(self):
        l = []
        for k, v in self.graph.iteritems():
            l.append(k)
        return l

    def edges(self):
        l = []
        for k, v in self.graph.iteritems():
            for edge in v:
                l.append([k, edge])
        return l

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

    def depth_first_helper(self, node, visited):
        visited.append(node)
        for edge in self.graph[node]:
            if edge not in visited:
                visited = self.depth_first_helper(edge, visited)
        return visited

    def depth_first_traversal(self, node):
        return self.depth_first_helper(node, [])

    def breadth_first_traversal(self, node):
        visited = []
        q = [node]
        while q:
            vertex = q.pop()
            if vertex not in visited:
                visited.append(vertex)
                for edge in self.graph[vertex]:
                    if edge not in visited:
                        q.append(edge)
        return visited








