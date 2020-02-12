import unittest

from classes import mars

class SimpleTest(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")
        
    def test_calculate_Weight(self):
        """
        Test that it can sum a list of integers
        """
        marsObj = mars.Mars()
        calculatedWeight = marsObj.calculateWeight(80)
        self.assertEqual(calculatedWeight, 30.26299694189602, "Should be 30.26299694189602")

if __name__ == '__main__':
    unittest.main()
