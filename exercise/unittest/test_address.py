import unittest
from unittest import TestCase
from address import Human 


class TestAge(TestCase):
    '''
    to avoid repeating create instance, use helper function setUp()
    '''
    def setUp(self):
        print('set up')
        self.person1= Human('chloe','ji', 28) #to make it as attribute instance 
        self.person2=Human('emma','emaily', 20)

    def tearDown(self):
        print('its done')

    def test_email(self):
        print('test email')
        self.assertEqual(self.person1.get_email, 'chloe_ji@gmail.com') 
        self.assertTrue(self.person1.get_email=='chloe_ji@gmail.com')

    def test_age(self):
        print('add age')
        self.assertEqual(self.person2.increase_amt(),48)

    def testInvalidType(self):
        print('test invalid')
        with self.assertRaises(TypeError):
            self.person1.get_email({}) 



if __name__=='__main__':
    unittest.main()  