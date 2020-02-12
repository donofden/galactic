import unittest

from classes import neptune

class NeptuneTest(unittest.TestCase):
        
    def test_calculate_weight_neptune(self):
        """
        Test 'calculateWeight'
        """
        Obj = neptune.Neptune()
        calculatedWeight = Obj.calculateWeight(80)
        # workaround: since the assertion of whole float value showing mismatching
        calculatedWeight = round(calculatedWeight, 2)
        self.assertEqual(calculatedWeight,90.93,"Should be 90.93")
