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

    def test_vertices_is_list(self):
        ''' Verifica que el retorno de la funcion vertices sea una lista '''
        vs = self.g.vertices()
        self.assertEqual( list, type( vs ) )

    def test_vertices_exist(self):
        ''' Todos los vertices incluidos en la lista existen en el grafo '''
        vs = ['v','w','x','y' ]
        self.assertEqual( sorted(vs), self.g.vertices() )

    def test_vertices_not_exist(self):
        ''' El vertice z no existe en el grafo generado en setup() '''
        vs =  ['v','w','x','y','z' ]
        self.assertNotEqual( sorted(vs), self.g.vertices() )

    def test_get_edge_exist(self):
        edge = self.g.get_edge(self.v, self.w)
        self.assertEqual(edge, self.e)

    def test_remove_edge_is_removed( self ):
        '''
        La prueba checa si el Edge esta por ahi.

        Depende de la funcion de get_edge
        '''
        edge = self.g.remove_edge( self.e )
        self.assertIsNone( self.g.get_edge( self.v, self.w ) )

if __name__ == '__main__':
    unittest.main()


