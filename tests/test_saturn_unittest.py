import unittest

from classes import saturn

class SaturnTest(unittest.TestCase):
        
    def test_calculate_weight_saturn(self):
        """
        Test 'calculateWeight'
        """
        Obj = saturn.Saturn()
        calculatedWeight = Obj.calculateWeight(80)
        # workaround: since the assertion of whole float value showing mismatching
        calculatedWeight = round(calculatedWeight, 2)
        self.assertEqual(calculatedWeight,85.14,"Should be 85.14")
