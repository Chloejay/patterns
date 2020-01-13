from unittest import TestCase, mock 
from attr import Price


class TestClassAttribute(TestCase):

    def test_patch_instance_attribute(self):
        price = Price()
        price.disc = 0.5
        price.qty=2
        self.assertAlmostEqual(price.after_discount(100), 100.0)

    def test_set_class_attribute(self):
        Price.disc= 0.75
        price = Price() 
        self.assertAlmostEqual(price.after_discount(100), 75.0)

    def test_patch_incorrect_class_attribute(self):
        with self.assertRaises(AttributeError):
            with mock.patch.object(Price, 'disc!!', 1):
                pass 

    def test_patch_class_attribute(self):
        with mock.patch.object(Price, 'disc', 0.85):
            price = Price()
            self.assertAlmostEqual(price.after_discount(100), 85) 