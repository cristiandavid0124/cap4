import unittest
import ejcap4 as cap4
import math


class TestCplxOperations(unittest.TestCase):
    def test_probposicion(self):
        v = [
            [[2, 1]],
            [[-1, 2]],
            [[0, 1]],
            [[1, 0]],
            [[3, -1]],
            [[2, 0]],
            [[0, -2]],
            [[-2, 1]],
            [[1, -3]],
            [[0, -1]]
        ]
        self.assertEqual(cap4.probposicion(v, 7), 10.869565217391305)

    def test_probvector(self):
        v1 = [
            [[2, 1]],
            [[-1, 2]],
            [[0, 1]],
            [[1, 0]],
            [[3, -1]],
            [[2, 0]],
            [[0, -2]],
            [[-2, 1]],
            [[1, -3]],
            [[0, -1]]
        ]
        v2 = [
            [[-1, -4]],
            [[2, -3]],
            [[-7, 6]],
            [[-1, 1]],
            [[-5, -3]],
            [[5, 0]],
            [[5, 8]],
            [[4, -4]],
            [[8, -7]],
            [[2, -7]]
        ]
        rt = (-0.020556626417313706, -0.1301919673096537)
        self.assertEqual(cap4.probvector(v1, v2), rt)

    def test_amplitudtransicion(self):
        v1 = [
            [[2, 1]],
            [[-1, 2]],
            [[0, 1]],
            [[1, 0]],
            [[3, -1]],
            [[2, 0]],
            [[0, -2]],
            [[-2, 1]],
            [[1, -3]],
            [[0, -1]]
        ]
        v2 = [
            [[-1, -4]],
            [[2, -3]],
            [[-7, 6]],
            [[-1, 1]],
            [[-5, -3]],
            [[5, 0]],
            [[5, 8]],
            [[4, -4]],
            [[8, -7]],
            [[2, -7]]
        ]
        rt = (-0.020556626417313706, -0.1301919673096537)
        self.assertEqual(cap4.amplitudtransicion(v1, v2), rt)

    def test_valoresperado(self):
        m = [
            [(3, 0), (1, 2)],
            [(1, -2), (-1, 0)]
        ]
        v = [
            [[math.sqrt(2) / 2, 0]],
            [[-math.sqrt(2) / 2, 0]]
        ]
        self.assertEqual(cap4.valoresperado(m, v), (0.0, 0.0))

    def test_operadordelta(self):
        m = [
            [(3, 0), (1, 2)],
            [(1, -2), (-1, 0)]
        ]
        v = [
            [[math.sqrt(2) / 2, 0]],
            [[-math.sqrt(2) / 2, 0]]
        ]
        rt = [[(3.0, 0.0), (1.0, 2.0)], [(1.0, -2.0), (-1.0, 0.0)]]
        self.assertEqual(cap4.operadordelta(m, v), rt)

    def test_variaza(self):
        m = [
            [(3, 0), (1, 2)],
            [(1, -2), (-1, 0)]
        ]
        v = [
            [[math.sqrt(2) / 2, 0]],
            [[-math.sqrt(2) / 2, 0]]
        ]
        self.assertEqual(cap4.varianza(m, v), (8.0, 0.0))

    def test_dinamica(self):
        m1 = [
            [(0, 0), (1, 0)],
            [(1, 0), (0, 0)]
        ]
        m2 = [
            [(math.sqrt(2) / 2, 0), (math.sqrt(2) / 2, 0)],
            [(math.sqrt(2) / 2, 0), (-(math.sqrt(2) / 2), 0)]
        ]
        v = [
            [[1, 0]],
            [[0, 0]]
        ]
        rt = [[(0.7071067811865476, 0.0)], [(-0.7071067811865476, 0.0)]]
        self.assertEqual(cap4.dinamica(m1, m2, v), rt)


if __name__ == '__main__':
    unittest.main()