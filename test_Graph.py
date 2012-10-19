import unittest

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


