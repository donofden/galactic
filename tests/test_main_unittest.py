import unittest
import main
import io

from unittest import mock
from unittest.mock import patch

class MainTest(unittest.TestCase):
    
    def test_print_out_utility(self):
        """
        Test 'calculateWeight'
        """
        with mock.patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            main.printOut('Earth', 80)
        self.assertEqual(fake_stdout.getvalue(),'Earth    : 80  \n')
        
    def test_weight_calculator(self):
        """
        Test 'calculateWeight'
        """
        # https://stackoverflow.com/questions/6271947/how-can-i-simulate-input-to-stdin-for-pyunit
        main.input = lambda _: 10
        wc = main.WeightCalculator()
        wc.get_weight()
        self.assertEqual(wc.weight, 10)
        
    def test_run(self):
        """
        Test 'calculateWeight'
        """
        # https://stackoverflow.com/questions/6271947/how-can-i-simulate-input-to-stdin-for-pyunit
        main.input = lambda _: 10
        wc = main.WeightCalculator()
        with mock.patch('sys.stdout', new=io.StringIO()) as fake_stdout:
            wc.run()
        self.assertEqual(fake_stdout.getvalue(),'\n\nEarth    : 10.0  \nMercury  : 3.78  \nVenus    : 9.04  \nMars     : 3.78  \nJupiter  : 25.27  \nSaturn   : 10.64  \nUranus   : 8.86  \nNeptune  : 11.37  \nPluto    : 0.66  \nSun      : 279.31  \n')
        self.assertEqual(wc.weight, 10)
