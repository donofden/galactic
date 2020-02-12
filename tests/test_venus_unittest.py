import unittest

from classes import venus

class VenusTest(unittest.TestCase):
        
    def test_calculate_weight_venus(self):
        """
        Test 'calculateWeight'
        """
        Obj = venus.Venus()
        calculatedWeight = Obj.calculateWeight(80)
        # workaround: since the assertion of whole float value showing mismatching
        calculatedWeight = round(calculatedWeight, 2)
        self.assertEqual(calculatedWeight,72.33,"Should be 72.33")
