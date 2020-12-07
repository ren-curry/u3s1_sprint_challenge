"""
Part 1 -  Keeping it Classy: Create `Product` class for the Acme Corporation
Part 2 -  Objects that Go!: Add Methods to `Product` class
Part 3 -  A Proper Inheritance: Create a subclass of `Product` `BoxingGlove`
"""
import random


class Product():
    """
    Base Product class for Acme Products.
    Attributes: name, price, weight, flammability, identifier
    Methods: stealability(), explode()
    """
    def __init__(self, name, price=10, weight=20, flammability=0.5):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = random.randint(1000000, 9999999)

    def stealability(self):
        """
        Method to determine if a product is "Stealable", which is based on
        (price/weight)
        """
        # Determine the stealability_ratio = price/weight
        stealability_ratio = self.price/self.weight

        # if/elif/else statement to return the Product stealability
        if(stealability_ratio < 0.5):
            return 'Not so stealable...'
        elif(stealability_ratio < 1.0):
            return 'Kinda stealable.'
        else:
            return 'Very stealable!'

    def explode(self):
        """
        Method to determine if a product will explode, which is based on
        (flammability*wieght)
        """
        # Determine the volatility = flammability * weight
        volatility = self.flammability * self.weight

        # if/elif/else statement to return if the Product will explode
        if(volatility < 10):
            return '...fizzle.'
        elif(volatility < 50):
            return '...boom!'
        else:
            return '...BABOOM!!'


class BoxingGlove(Product):
    """
    Class for BoxingGlove inheriting from base class Products
    Attributes: name, price, weight, flammability, identifier
    Methods: stealability(), explode(), punch()
    """
    def __init__(self, name, price=10, weight=10, flammability=0.5):
        super().__init__(name, price, weight, flammability)

    # Overrides explode function from base class
    def explode(self):
        return "...it's a glove."

    def punch(self):
        if(self.weight < 5):
            return 'That Tickles.'
        elif(self.weight < 15):
            return 'Hey that hurt!'
        else:
            return 'OUCH!'
