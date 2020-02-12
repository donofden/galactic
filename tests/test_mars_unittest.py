import unittest

from classes import mars

class MarsTest(unittest.TestCase):
        
    def test_calculate_weight(self):
        """
        Test 'calculateWeight'
        """
        marsObj = mars.Mars()
        calculatedWeight = marsObj.calculateWeight(80)
        self.assertEqual(calculatedWeight, 30.26299694189602, "Should be 30.26299694189602")

