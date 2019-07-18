"""
We need to write some code to return the original price of a product, the return type must be of type decimal and the number must be rounded to two decimal places.

We will be given the sale price (discounted price), and the sale percentage, our job is to figure out the original price.

For example:
Given an item at $75 sale price after applying a 25% discount, the function should return the original price of that item before applying the sale percentage, which is ($100.00) of course, rounded to two decimal places.

DiscoverOriginalPrice(75, 25) => 100.00M where 75 is the sale price (discounted price), 25 is the sale percentage and 100 is the original price
"""
"""Results:
Test.describe("Basic tests")
Test.assert_equals(discover_original_price(75,25),100)
Test.assert_equals(discover_original_price(25,75),100)
Test.assert_equals(discover_original_price(75.75,25),101)
Test.assert_equals(discover_original_price(373.85,11.2),421)
Test.assert_equals(discover_original_price(458.2,17.13),552.91)"""

def discover_original_price(discounted_price, sale_percentage):
    #your code here
    original_price = discounted_price / (((sale_percentage/100) - 1)* -1)
    return round(original_price, 2)


"""
Liked:
def discover_original_price(discounted_price, sale_percentage):
    return round(discounted_price / ((100 - sale_percentage) * 0.01), 2)
"""