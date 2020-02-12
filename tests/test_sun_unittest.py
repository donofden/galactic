import unittest

from classes import sun

class SunTest(unittest.TestCase):
        
    def test_calculate_weight_sun(self):
        """
        Test 'calculateWeight'
        """
        Obj = sun.Sun()
        calculatedWeight = Obj.calculateWeight(80)
        # workaround: since the assertion of whole float value showing mismatching
        calculatedWeight = round(calculatedWeight, 2)
        self.assertEqual(calculatedWeight,2234.45,"Should be 2234.45")
