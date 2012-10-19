import unittest
from Graph import Graph, Vertex, Edge

class GraphTest(unittest.TestCase):

    def setUp(self):
        self.v = Vertex('v')
        self.w = Vertex('w')
        self.x = Vertex('x')
        self.y = Vertex('y')
        self.z = Vertex('z')
        self.e = Edge(self.v, self.w)
        self.e2 = Edge(self.v, self.x)
        self.g = Graph([self.v, self.w ,self.x, self.y],[self.e, self.e2])

    def test_get_edge_not_exist(self):
        edge = self.g.get_edge(self.v, self.y)
        self.assertIsNone(edge)

    def test_get_edge_exist(self):
        edge = self.g.get_edge(self.v, self.w)
        self.assertEqual(edge, self.e)

if __name__ == '__main__':
    unittest.main()


