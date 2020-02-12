import unittest

from classes import jupiter

class JupiterTest(unittest.TestCase):
        
    def test_calculate_weight_jupiter(self):
        """
        Test 'calculateWeight'
        """
        jupiterObj = jupiter.Jupiter()
        calculatedWeight = jupiterObj.calculateWeight(80)
        
        # workaround: since the assertion of whole float value showing miss matching
        calculatedWeight = round(calculatedWeight, 2)
        
        self.assertEqual(calculatedWeight,202.16,"Should be 202.16")
