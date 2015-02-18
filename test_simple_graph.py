import pytest
from simple_graph import Graph
@pytest.fixture
def populated():
    g = Graph()
    g.add_node(5)
    g.add_node(7)
    g.add_node("Hello")
    g.add_edge(5, 7)
    g.add_edge(5, "Hello")
    return g


def test_graph_constructor():
    assert Graph().graph == {}


def test_nodes(populated):
    for val in [5, 7, "Hello"]:
        assert val in populated.graph
    assert 27 not in populated.graph


def test_edges(populated):
    assert populated.edges() == [[5, 7], [5, "Hello"]]


def test_add_node():
    g = Graph()
    g.add_node(70)
    assert 70 in g.graph


def test_add_mutable(populated):
    with pytest.raises(TypeError):
        populated.add_node([1, 3])


def test_add_edge(populated):
    populated.add_edge(7, 5)
    assert [7, 5] in populated.edges()


def test_del_node(populated):
    populated.del_node(5)
    assert 5 not in populated.graph


def test_del_edge(populated):
    populated.del_edge(5, 7)
    assert [5, 7] not in populated.edges()


def test_has_node(populated):
    assert populated.has_node(5)


def test_doesnt_have_node(populated):
    assert not populated.has_node(39)


def test_neighbors(populated):
    assert populated.neighbors(5) == [7, "Hello"]


def test_neigbors_none(populated):
    with pytest.raises(KeyError):
        populated.neighbors(58)


def test_adjacent(populated):
    assert populated.adjacent(5, 7)


def test_adjacent_none(populated):
    with pytest.raises(KeyError):
        populated.adjacent(58, 28)
