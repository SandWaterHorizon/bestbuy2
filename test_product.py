# test_product.py
import pytest
from products import Product, NonStockedProduct


"""
Test that creating a normal product works.

Test that creating a product with invalid details (empty name, negative price) invokes an exception.

Test that when a product reaches 0 quantity, it becomes inactive.

Test that product purchase modifies the quantity and returns the right output.

Test that buying a larger quantity than exists invokes exception.

EXAMPLE
# Empty name
Product("", price=1450, quantity=100)

# Negative Price
Product("MacBook Air M2", price=-10, quantity=100)
"""



def test_creating_prod():
    product = Product("Laptop", price=1000, quantity=10)
    assert product.name == "Laptop"
    assert product.price == 1000
    assert product.quantity == 10
    assert product.is_active() is True


def test_creating_prod_invalid_details():
    with pytest.raises(ValueError):
        Product("", price=1450, quantity=100)  # Empty name should raise an exception

    with pytest.raises(ValueError):
        Product("MacBook Air M2", price=-10, quantity=100)  # Negative price should raise an exception


def test_prod_becomes_inactive():
    product = Product("Smartphone", price=500, quantity=1)
    product.buy(1)
    assert product.quantity == 0
    assert product.is_active() is False


def test_buy_modifies_quantity():
    product = Product("Tablet", price=300, quantity=5)
    product.buy(2)
    assert product.quantity == 3


def test_buy_too_much():
    product = Product("Headphones", price=50, quantity=2)
    with pytest.raises(ValueError):
        product.buy(3)

def test_non_stocked_product():
    product = NonStockedProduct("Windows License", price=125)
    assert product.get_quantity() == 0  # Should have 0 quantity
    assert product.is_active() is True  # Should be active, no stock constraints

    # Non-stocked product can always be purchased, so test that buying it works
    total_price = product.buy(5)  # No error should occur
    assert total_price == 125 * 5  # Total price should be 125 * 5 = 625

    # Test that setting quantity is not allowed for non-stocked products
    with pytest.raises(ValueError):
        product.set_quantity(10)  # Should raise a ValueError since quantity cannot be set

