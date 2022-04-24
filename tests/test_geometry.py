from mathematics import geometry
import unittest
import math
import pytest

class TestGeometry(unittest.TestCase):
    def test_kwad1(self):
        assert geometry.pole_kwadrat(2) == 4
    def test_kwad2(self):
        assert geometry.pole_kwadrat(0.5) == 0.25
    def test_pros1(self):
        assert geometry.pole_prostokat(3,4) == 12
    def test_pros2(self):
        assert geometry.pole_prostokat(4,2.2) == 8.8
    def test_troj1(self):
        assert geometry.pole_trojkat(2,4) == 4
    def test_troj2(self):
        assert geometry.pole_trojkat(3,1) == 1.5
    def test_kolo1(self):
        assert geometry.pole_kolo(4) == 16*math.pi