"""
Part 5 - Measure twice, Test once: Where we implement testing for
    the Challenge assignment
"""
import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_default_product_weight(self):
        """Test default product weight being 20."""
        prod = Product('Test Product')
        self.assertEqual(prod.weight, 20)

    def test_default_product_flammability(self):
        """Test default product flammability being 0.5."""
        prod = Product('Test Product')
        self.assertEqual(prod.flammability, 0.5)

    def test_default_product_stealability(self):
        """Test stealability() returns the correct messages."""
        prod1 = Product('Test Product 1', price=5, weight=20)
        prod2 = Product('Test Product 2', price=15, weight=20)
        prod3 = Product('Test Product 3', price=25, weight=20)
        self.assertEqual(prod1.stealability(), 'Not so stealable...')
        self.assertEqual(prod2.stealability(), 'Kinda stealable.')
        self.assertEqual(prod3.stealability(), 'Very stealable!')

    def test_default_product_explode(self):
        """Test explode() returns the correct messages."""
        prod1 = Product('Test Product 1', weight=15, flammability=0.5)
        prod2 = Product('Test Product 2', weight=20, flammability=1.0)
        prod3 = Product('Test Product 3', weight=25, flammability=2.5)
        self.assertEqual(prod1.explode(), '...fizzle.')
        self.assertEqual(prod2.explode(), '...boom!')
        self.assertEqual(prod3.explode(), '...BABOOM!!')


class AcmeReportTests(unittest.TestCase):
    """Making sure Acme reports are the tops!"""
    def test_default_generate_products(self):
        """Test generate_products() returns 30 products by default"""
        prods = generate_products()
        self.assertEqual(len(prods), 30)

    def test_legal_names(self):
        """Test the generated names of products are legal."""
        prods = generate_products()
        prod_names = [prod.name.split(' ') for prod in prods]
        self.assertEqual(len(prod_names[0]), 2)
        for name in prod_names:
            self.assertIn(name[0], ADJECTIVES)
            self.assertIn(name[1], NOUNS)


if __name__ == '__main__':
    unittest.main()
