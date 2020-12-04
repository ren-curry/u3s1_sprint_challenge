"""
Part 4 -  Class Report: Generate Products and report on them
"""
import random
from acme import Product

# Variable Definitions for use throughout code
ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(number_of_products=30):
    # Variable definitions for this function
    products = []
    counter = 0

    while(counter < number_of_products):
        name = random.choice(ADJECTIVES) + ' ' + random.choice(NOUNS)
        price = random.randint(5, 100)
        weight = random.randint(5, 100)
        flammability = random.uniform(0.0, 2.5)

        products.append(Product(name, price, weight, flammability))
        counter += 1

    return products


def inventory_report(products):
    # Variable Definitions
    unique_products = []
    count_unique_products = 0
    avg_price = 0
    avg_weight = 0
    avg_flammability = 0

    # Create a list of unique product names to count
    for product in products:
        if product.name not in unique_products:
            unique_products.append(product.name)
    count_unique_products = len(unique_products)

    # Calculate the averages using generator expressions.
    avg_price = (sum(product.price for product in products)
                 / float(len(products)))
    avg_weight = (sum(product.weight for product in products)
                  / float(len(products)))
    avg_flammability = (sum(product.flammability for product in products)
                        / float(len(products)))

    # Print the Report results
    print('ACME CORPORATION OFFICIAL INVENTORY REPORT')
    print(f'Unique product names: {count_unique_products}')
    print(f'Average price: {avg_price}')
    print(f'Average weight: {avg_weight}')
    print(f'Average flammability: {avg_flammability}')


if __name__ == '__main__':
    inventory_report(generate_products())
