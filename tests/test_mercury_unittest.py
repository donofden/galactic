import unittest

from classes import mercury

class MercuryTest(unittest.TestCase):
        
    def test_calculate_weight_mercury(self):
        """
        Test 'calculateWeight'
        """
        Obj = mercury.Mercury()
        calculatedWeight = Obj.calculateWeight(80)
        # workaround: since the assertion of whole float value showing mismatching
        calculatedWeight = round(calculatedWeight, 2)
        self.assertEqual(calculatedWeight,30.20,"Should be 30.20")
