import unittest

from classes import uranus

class UranusTest(unittest.TestCase):
        
    def test_calculate_weight_uranus(self):
        """
        Test 'calculateWeight'
        """
        Obj = uranus.Uranus()
        calculatedWeight = Obj.calculateWeight(80)
        # workaround: since the assertion of whole float value showing mismatching
        calculatedWeight = round(calculatedWeight, 2)
        self.assertEqual(calculatedWeight,70.87,"Should be 70.87")
