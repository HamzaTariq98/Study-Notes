import unittest
import main


class TestMain(unittest.TestCase):

    def setUp(self): # Here u may define all variables before run tests
        pass 
    def test_do_stuff(self):
        test_param = '10' # even if entered number is str we still can run our code and get result equal to 15
        result = main.do_stuff(test_param)
        self.assertEqual(result,15)

    def test_do_stuff2(self):
        test_param = 'aaaa'
        result = main.do_stuff(test_param) # return Error type object if test_param is 'aaa'
        self.assertIsInstance(result,ValueError) # if Error type object is ValueError, the test is success
    
    def tearDown(self):
        print('\nEnd of each test')
if __name__ == '__main__':
    unittest.main()
