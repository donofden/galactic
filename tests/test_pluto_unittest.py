import unittest

from classes import pluto

class PlutoTest(unittest.TestCase):
        
    def test_calculate_weight_pluto(self):
        """
        Test 'calculateWeight'
        """
        Obj = pluto.Pluto()
        calculatedWeight = Obj.calculateWeight(80)
        # workaround: since the assertion of whole float value showing mismatching
        calculatedWeight = round(calculatedWeight, 2)
        self.assertEqual(calculatedWeight,5.3,"Should be 5.3")
