# store.py

from products import Product, NonStockedProduct  # Assuming Product and NonStockedProduct class is in product.py



class Store:
    """
    The Store class holds a collection of products and provides methods to
    manage them and process orders.
    """

    def __init__(self, products=None):
        """
        Initializes the store with a list of products.
        If no products are provided, initializes with an empty list.
        """
        self.products = products if products else []

    def add_product(self, product):
        """
        Adds a product to the store.
        """
        self.products.append(product)

    def remove_product(self, product):
        """
        Removes a product from the store if it exists.
        """
        if product in self.products:
            self.products.remove(product)

    def get_total_quantity(self):
        """
        Returns the total number of items available in the store.
        """
        return sum(product.get_quantity() for product in self.products)

    def get_all_products(self):
        """
        Returns a list of all active products in the store.
        """
        return [product for product in self.products if product.is_active()]

    def order(self, shopping_list):
        """
        Processes an order given a list of (Product, quantity) tuples.
        Returns the total price of the order.
        Raises an exception if a product is out of stock or if quantity requested is invalid.
        """
        total_price = 0.0
        for product, quantity in shopping_list:
            if isinstance(product, NonStockedProduct):
                total_price += product.buy(quantity)  # No stock check for non-stocked products
            else:
                total_price += product.buy(quantity)  # Standard stock checking for other products
        return total_price


if __name__ == "__main__":
    product_list = [
        Product("MacBook Air M2", price=1450, quantity=100),
        Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        Product("Google Pixel 7", price=500, quantity=250),
        NonStockedProduct("Windows License", price=125),  # Non-stocked product added
    ]

    store = Store(product_list)
    products = store.get_all_products()

    print("Total Quantity in Store:", store.get_total_quantity())  # Output: Total quantity of all active products
    try:
        print("Order Cost:", store.order([(products[0], 1), (products[1], 2), (products[3], 2)]))  # Processes an order with a non-stocked product
    except ValueError as e:
        print(f"Order failed: {e}")  # Catch and display any error




