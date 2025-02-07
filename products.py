# products.py
class Product:
    """
    Class Specification
    Instance variables:
    Name (str)
    Price (float)
    Quantity (int)
    Active (bool)
    """

    def __init__(self, name: str, price: float, quantity: int):
        if not name:
            raise ValueError("Product name cannot be empty")
        if price < 0:
            raise ValueError("Price cannot be negative")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True  # Product is active by default

    def __str__(self):
        return f"{self.name} - ${self.price} ({self.quantity} available)"

    def set_quantity(self, quantity: int):
        """
        Setter function for quantity.
        If quantity reaches 0, deactivates the product.
        """
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()  # Deactivates product if quantity is 0

    def get_quantity(self) -> int:
        """
        Getter function for quantity.
        Returns the quantity.
        """
        return self.quantity

    def is_active(self) -> bool:
        """
        Getter function for active.
        Returns True if the product is active, otherwise False.
        """
        return self.active

    def activate(self):
        """
        Activates the product.
        """
        self.active = True

    def deactivate(self):
        """
        Deactivates the product.
        """
        self.active = False

    def show(self) -> str:
        """
        Returns a string that represents the product.
        Example: "MacBook Air M2, Price: 1450, Quantity: 100"
        """
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def buy(self, quantity: int) -> float:
        """
        Buys a given quantity of the product.
        Returns the total price (float) of the purchase.
        Updates the quantity of the product.
        Raises an Exception if the requested quantity is not available.
        """
        if quantity <= 0:
            raise ValueError("Quantity to buy must be greater than zero")
        if quantity > self.quantity:
            raise ValueError("Not enough stock available")

        total_price = quantity * self.price
        self.set_quantity(self.quantity - quantity)  # Reduce stock

        return total_price


class NonStockedProduct(Product):
    def __init__(self, name: str, price: float):
        super().__init__(name, price, quantity=0)  # Non-stocked products have 0 quantity

    def buy(self, quantity: int) -> float:
        # Allow purchase of any quantity for non-stocked products
        if quantity <= 0:
            raise ValueError("Quantity to buy must be greater than zero")
        total_price = quantity * self.price
        return total_price  # No need to reduce stock since it's non-stocked

    def show(self) -> str:
        return f"{self.name}, Price: {self.price} (Non-stocked product)"

    def set_quantity(self, quantity: int):
        # Non-stocked products cannot have their quantity set
        raise ValueError("Cannot set quantity for non-stocked products.")


class LimitedProduct(Product):
    def __init__(self, name: str, price: float, quantity: int, maximum: int):
        super().__init__(name, price, quantity)
        self.maximum = maximum

    def buy(self, quantity: int) -> float:
        if quantity > self.maximum:
            raise ValueError(f"Cannot buy more than {self.maximum} at a time.")
        return super().buy(quantity)

    def show(self) -> str:
        return f"{self.name}, Price: {self.price}, Max per order: {self.maximum}"
