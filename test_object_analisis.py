""" 2. Write a test for each function that demonstrate the problem """
import json
import unittest
from object_analisis import aboundant, farthest

class TestObjectAnalisis(unittest.TestCase):
    """
    Our basic test class
    Any method which starts with ``test_`` will considered as a test case.
    """

    def test_aboundant(self):
        """
        The actual test case for function aboundant.
        Actual result is the value returned from executing the function.
        Expected result is the correct value.
        In order to pass the test, the actual should be equal to expected result
        """
        input = """
        [
        {
            "type": "frb",
            "name": "crab",
            "redshift": 0
        }
        ]
        """
        actual = aboundant(json.loads(input))
        self.assertEqual(actual, 'frbs') # actual should be equal to expected



    def test_farthest(seft):
        """
        The actual test case for function farthest.
        Actual result is the value returned from executing the function.
        Expected result is the correct value.
        In order to pass the test, the actual should be equal to expected result
        """
        print("hello")
        input = """
        [
            {
                "type": "star",
                "name": "alpha-centaurus",
                "redshift": 0
            },
            {
                "type": "nebula",
                "name": "crab",
                "redshift": 4
            }
        ]
        """
        actual = farthest(json.loads(input))
        expected = {
                "type": "nebula",
                "name": "crab",
                "redshift": 4
            }
        seft.assertEqual(actual, expected) # actual should be equal to expected

    
if __name__ == '__main__':
    unittest.main()