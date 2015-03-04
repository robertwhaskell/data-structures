import pytest
from simple_graph import Graph


@pytest.fixture
def populated():
    g = Graph()
    g.add_node(5)
    g.add_node(7)
    g.add_node("Hello")
    g.add_edge(5, 7, 30)
    g.add_edge(5, "Hello", 10)
    return g


@pytest.fixture
def cyclic():
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
    g.add_edge(1, 2, 1)
    g.add_edge(1, 3, 3)
    g.add_edge(1, 6, 3)
    g.add_edge(5, 1, 10)
    g.add_edge(2, 8, 1000)
    g.add_edge(2, 9, 1)
    g.add_edge(2, 4, 4)
    g.add_edge(2, 3, 50)
    g.add_edge(3, 7, 4)
    g.add_edge(7, 1, 5)
    g.add_edge(7, 6, 10)
    return g


def test_graph_constructor():
    assert Graph().graph == {}


def test_nodes(populated):
    for val in [5, 7, "Hello"]:
        assert val in populated.graph
    assert 27 not in populated.graph


def test_edges(populated):
    edge_list = populated.edges()
    assert len(edge_list) == 2
    assert [5, 7, 30] in edge_list
    assert [5, "Hello", 10] in edge_list


def test_add_node():
    g = Graph()
    g.add_node(70)
    assert 70 in g.graph


def test_add_mutable(populated):
    with pytest.raises(TypeError):
        populated.add_node([1, 3])


def test_add_edge(populated):
    populated.add_edge(7, 5, 10)
    assert [7, 5, 10] in populated.edges()


def test_add_edge_new_node(populated):
    populated.add_edge(5, 28, 1000)
    assert 28 in populated.graph
    assert 28 in populated.graph[5]


def test_del_node(populated):
    populated.del_node(5)
    assert 5 not in populated.graph
    for k, v in populated.graph.iteritems():
            assert 5 not in v


def test_del_nonexistent_node(populated):
    with pytest.raises(KeyError):
        populated.del_node(70)


def test_del_edge(populated):
    populated.del_edge(5, 7)
    assert [5, 7] not in populated.edges()


def test_del_nonexistent_edge(populated):
    with pytest.raises(KeyError):
        populated.del_edge(5, 10)
    with pytest.raises(KeyError):
        populated.del_edge(10, 5)


def test_del_node_edge_list(cyclic):
    cyclic.del_node(3)
    assert 3 not in cyclic.graph[1]


def test_has_node(populated):
    assert populated.has_node(5)


def test_doesnt_have_node(populated):
    assert not populated.has_node(39)


def test_neighbors(populated):
    assert populated.neighbors(5) == {7: 30, "Hello": 10}


def test_neigbors_none(populated):
    with pytest.raises(KeyError):
        populated.neighbors(58)


def test_adjacent(populated):
    assert populated.adjacent(5, 7)


def test_adjacent_none(populated):
    with pytest.raises(KeyError):
        populated.adjacent(58, 28)


def test_depth_first(cyclic):
    nodes = cyclic.depth_first_traversal(1)
    for val in [1, 2, 3, 4, 6, 7, 8, 9]:
        assert val in nodes


def test_breadth_first(cyclic):
    nodes = cyclic.breadth_first_traversal(1)
    for val in [1, 2, 3, 4, 6, 7, 8, 9]:
        assert val in nodes


def test_dijkstras_algorithm(populated):
    assert populated.dijkstras_algorithm(5) == {7: 5, "Hello": 5}
