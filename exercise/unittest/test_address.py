import unittest 
from file import Human 

# make all the test units isolated from each other 
# TODO mocks 

class TestAge(unittest.TestCase):
    '''
    to avoid to repeat the 
    person1= Human('chloe','ji', 28), make two helper function def setUp() and tearDown() 
    '''
    def setUp(self):
        print('set up')
        self.person1= Human('chloe','ji', 28) #to make it as the attribute instance 
        self.person2=Human('emma','emaily', 20)

    def tearDown(self):
        print('its done')

    def test_email(self):
        print('test email')
        self.assertEqual(self.person1.get_email, 'chloe_ji@gmail.com') 

    def test_age(self):
        print('add age')
        self.assertEqual(self.person2.increase_amt(),48)

if __name__=='__main__':
    unittest.main()  