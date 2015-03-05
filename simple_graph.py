class Graph(object):

    def __init__(self):
        self.graph = {}

    def nodes(self):
        """Return a list of nodes in the graph."""
        return self.graph.keys()

    def edges(self):
        """Return a list of edges and their weights in the graph."""
        l = []
        for k, v in self.graph.iteritems():
            for node in v:
                l.append([k, node, v[node]])
        return l

    def add_node(self, node):
        """Add a node to the graph."""
        self.graph.setdefault(node, {})

    def add_edge(self, node1, node2, weight):
        """Add an edge to the graph."""
        try:
            self.graph.setdefault(node2, {})
            self.graph[node1].setdefault(node2, weight)
        except KeyError:
            self.graph.setdefault(node1, {node2: weight})

    def del_node(self, node):
        """
        Delete a node from the graph. Throw a KeyError if the node wasn't
        in the graph.
        """
        try:
            self.graph.pop(node)
        except KeyError:
            raise KeyError("{} does not exist".format(node))
        for k, v in self.graph.iteritems():
            if node in v:
                v.pop(node)

    def del_edge(self, node1, node2):
        """
        Delete an edge from the graph. Throw a KeyError if either node
        wasn't in the graph.
        """
        temp = ''
        try:
            temp = self.graph[node1]
        except KeyError:
            raise KeyError("{} does not exist".format(node1))
        try:
            temp.pop(node2)
        except KeyError:
            raise KeyError("{} does not exist".format(node2))

    def has_node(self, node):
        """Return True if node is in graph."""
        return node in self.graph

    def neighbors(self, node):
        """
        Return a dictionary of nodes connected to the supplied node. Throw
        a KeyError if the supplied node wasn't in the graph.
        """
        try:
            return self.graph[node]
        except KeyError:
            raise KeyError("{} doesn't exist".format(node))

    def adjacent(self, node1, node2):
        """
        Return true if an edge points from the first node to the second
        node. Throw a KeyError if the first node wasn't in the graph.
        """
        try:
            return node2 in self.graph[node1]
        except KeyError:
            raise KeyError("{} doesn't exist".format(node1))

    def _depth_first_helper(self, node, visited):
        visited.append(node)
        for edge in self.graph[node]:
            if edge not in visited:
                visited = self._depth_first_helper(edge, visited)
        return visited

    def depth_first_traversal(self, node):
        """
        Perform a depth-first traversal of the graph. Return a list of
        nodes in the order visited.
        """
        return self._depth_first_helper(node, [])

    def breadth_first_traversal(self, node):
        """
        Perform a breadth-first traversal of the graph. Return a list of
        nodes in the order visited.
        """
        visited = []
        q = [node]
        while len(q) > 0:
            vertex = q.pop(0)
            if vertex not in visited:
                visited.append(vertex)
                for edge in self.graph[vertex]:
                    if edge not in visited:
                        q.append(edge)
        return visited

    def dijkstras_algorithm(self, source):
        dist = {}
        prev = {}
        uv = {}

        for key, val in self.graph.iteritems():
            dist[key] = float("inf")
            prev[key] = None
            uv.setdefault(key, val)
        dist[source] = 0
        while uv:
            next = min(uv, key=dist.get)
            for neighbor, distance in uv[next].iteritems():
                alt = dist[next] + distance
                if alt < dist[neighbor]:
                    dist[neighbor] = alt
                    prev[neighbor] = next
            uv.pop(next)

        return dist, prev

    def bellman_ford_algorithm(self, source):
        dist = {}
        prev = {}

        for node in self.nodes():
            if node == source:
                dist[node] = 0
            else:
                dist[node] = float("inf")
                prev[node] = None

        for node in self.nodes():
            for node1, node2, weight in self.edges():
                if dist[node1] + weight < dist[node2]:
                    dist[node2] = dist[node1] + weight
                    prev[node2] = node1

        for node1, node2, weight in self.edges():
            if dist[node1] + weight < dist[node2]:
                raise ValueError("Graph contains a negative-weight cycle")

        return dist, prev


def construct_cyclic_graph():
    g = Graph()
    g.add_node(1)
    g.add_node(2)
    g.add_node(3)
    g.add_node(4)
    g.add_node(5)
    g.add_node(6)
    g.add_node(7)
    g.add_node(8)
    g.add_node(9)
    g.add_edge(1, 2, 4)
    g.add_edge(1, 3, 2)
    g.add_edge(1, 6, 1)
    g.add_edge(5, 1, 3)
    g.add_edge(2, 8, 5)
    g.add_edge(2, 9, 6)
    g.add_edge(2, 4, 3)
    g.add_edge(2, 3, 1)
    g.add_edge(3, 7, 6)
    g.add_edge(7, 1, 2)
    g.add_edge(7, 6, 5)
    return g


def construct_different_graph():
    g = Graph()
    g.graph.setdefault(2, {6: 2, 3: 4})
    g.graph.setdefault(1, {5: 1, 2: 3})
    g.graph.setdefault(3, {})
    g.graph.setdefault(4, {1: 5})
    g.graph.setdefault(5, {4: 1, 2: 4, 6: 3})
    g.graph.setdefault(6, {1: 2, 5: 6, 3: 1, 2: 3})
    return g


def measure_runtime(my_function):
    import datetime
    start_time = datetime.datetime.now()
    my_function(1)
    end_time = datetime.datetime.now()
    return (end_time - start_time)


if __name__ == '__main__':
    g = construct_cyclic_graph()
    print "Time for depth-first traversal:"
    print measure_runtime(g.depth_first_traversal)
    print "Time for breadth-first traversal:"
    print measure_runtime(g.breadth_first_traversal)
    e = construct_different_graph()
    print "Trying for a new graph."
    print "Time for depth-first traversal:"
    print measure_runtime(e.depth_first_traversal)
    print "Time for breadth-first traversal:"
    print measure_runtime(e.breadth_first_traversal)
