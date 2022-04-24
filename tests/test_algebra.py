from mathematics import algebra
import unittest
import pytest

class TestAlgebra(unittest.TestCase):
    def test_add1(self):
        assert algebra.add(2, 3) == 5
    def test_add2(self):
        self.assertEqual(algebra.add(7, 8), 15)
    def test_add3(self):
        self.assertEqual(algebra.add(0.5, 3), 3.5)
    def test_sub1(self):
        self.assertEqual(algebra.sub(4, 3), 1)
    def test_sub2(self):
        self.assertEqual(algebra.sub(5, 0.8), 4.2)
    def test_sub3(self):
        self.assertEqual(algebra.sub(1, 4), -3)
    def test_mul1(self):
        self.assertEqual(algebra.mul(4, 3), 12)
    def test_mul2(self):
        self.assertEqual(algebra.mul(4, 0), 0)
    def test_mul3(self):
        self.assertEqual(algebra.mul(1.5, 3), 4.5)
    def test_div1(self):
        self.assertEqual(algebra.div(4, 2), 2)
    def test_div2(self):
        self.assertEqual(algebra.div(5, 0), "Nie można dzielić przez zero")
    def test_div3(self):
        self.assertEqual(algebra.div(1.5, 3), 0.5)
    def test_mat1(self):
        self.assertEqual(algebra.add_matrices([[1,2],[3,4]], [[6,7],[8,9]]), [[7,9],[11,13]])
    def test_kwad1(self):
        self.assertEqual(algebra.rown_kwadratowe(1,5,6), [-2,-3])
    def test_kwad2(self):
        self.assertEqual(algebra.rown_kwadratowe(1,4,4), [-2])
    def test_kwad3(self):
        self.assertEqual(algebra.rown_kwadratowe(1,1,4), "Brak pierwiastków")

