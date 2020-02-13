import unittest
import main
import io

from unittest import mock
from unittest.mock import patch
import io


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
        self.assertEqual(fake_stdout.getvalue(),'Earth    : 10  \nMercury  : 3.78  \nVenus    : 9.04  \nMars     : 3.78  \nJupiter  : 25.27  \nSaturn   : 10.64  \nUranus   : 8.86  \nNeptune  : 11.37  \nPluto    : 0.66  \nSun      : 279.31  \n')
        self.assertEqual(wc.weight, 10)


''' Testing input() and print()

testing print()

from nose.tools import *
from unittest import mock
from unittest.mock import patch
import io

def foo():
    print("Something")

# Solution one: testing print with @patch
@patch('sys.stdout', new_callable=io.StringIO)
def test_foo_one(mock_stdout):
    foo()
    assert mock_stdout.getvalue() == 'Something\n'

# Solution two: testing print with with-statement
def test_foo_two():
    with mock.patch('sys.stdout', new=io.StringIO()) as fake_stdout:
        foo()

    assert fake_stdout.getvalue() == 'Something\n'

# Solution three: testing print with with-statement
# and assert_has_calls
def test_foo_three():
    with mock.patch('sys.stdout') as fake_stdout:
        foo()

    fake_stdout.assert_has_calls([
        mock.call.write('Something'),
        mock.call.write('\n')
    ])
'''

''' testing input()

from nose.tools import *
from unittest import mock

def bar():
    ans = input("enter yes or no")
    if ans == "yes":
        return "you entered yes"
    if ans == "no":
        return "you entered no"


def test_bar_yes():
    original_input = mock.builtins.input
    mock.builtins.input = lambda _: "yes"
    assert_equal(bar(), "you entered yes")
    mock.builtins.input = original_input

def test_bar_no():
    original_input = mock.builtins.input
    mock.builtins.input = lambda _: "no"
    assert_equal(bar(), "you entered no")
    mock.builtins.input = original_input
    
Some usefull ressources:

https://stackoverflow.com/questions/3622455/what-is-the-purpose-of-mock-objects#3623574
https://stackoverflow.com/questions/21046717/python-mocking-raw-input-in-unittests
https://stackoverflow.com/questions/32488280/unit-testing-for-user-input-and-expected-output-in-python
https://stackoverflow.com/questions/46222661/how-to-mock-a-user-input-in-python
http://blog.thedigitalcatonline.com/blog/2016/09/27/python-mocks-a-gentle-introduction-part-2/
https://stackoverflow.com/questions/25677260/python-unit-test-for-nested-if-statement#25677484
https://stackoverflow.com/questions/15391504/how-to-unit-test-an-if-else-statement-in-c-sharp-using-just-a-stubclass
https://stackoverflow.com/questions/18161330/using-unittest-mock-to-patch-input-in-python-3
https://stackoverflow.com/questions/12998908/is-it-possible-to-mock-pythons-built-in-print-function


Python Mocking 101: Fake It Before You Make It -> https://www.fugue.co/blog/2016-02-11-python-mocking-101


'''