# products.py



class Promotion:
    def __init__(self, name: str):
        self.name = name

    def apply_promotion(self, product, quantity: int) -> float:
        raise NotImplementedError("This method should be overridden by subclasses.")


class PercentDiscount(Promotion):
    def __init__(self, name: str, percent: float):
        super().__init__(name)
        self.percent = percent

    def apply_promotion(self, product, quantity: int) -> float:
        total_price = quantity * product.price
        discount = total_price * (self.percent / 100)
        final_price = total_price - discount
        print(f"{self.name} Applied: Total price for {quantity} items = {final_price}")
        return final_price


class SecondHalfPrice(Promotion):
    def __init__(self, name: str):
        super().__init__(name)

    def apply_promotion(self, product, quantity: int) -> float:
        if quantity >= 2:
            # Apply second half-price for all items after the first one
            total_price = product.price + (product.price * (quantity - 1) / 2)
            print(f"Second Half Price Applied: Total price for {quantity} items = {total_price}")
            return total_price
        else:
            total_price = quantity * product.price
            print(f"No discount applied, price for {quantity} items = {total_price}")
            return total_price


class ThirdOneFree(Promotion):
    def __init__(self, name: str):
        super().__init__(name)

    def apply_promotion(self, product, quantity: int) -> float:
        free_items = quantity // 3  # Get one free for every 3 items
        total_price = (quantity - free_items) * product.price
        return total_price


class Product:
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
        self.promotion = None  # Default is no promotion


    def get_quantity(self):
        return self.quantity

    def is_active(self):
        return self.quantity > 0

    def set_promotion(self, promotion: Promotion):
        self.promotion = promotion

    def get_promotion(self):
        return self.promotion

    def __str__(self):
        promotion_info = f" Promotion: {self.promotion.name}" if self.promotion else " No promotion"
        return f"{self.name}, Price: {self.price} (Stock: {self.quantity}){promotion_info}"

    def show(self):
        return str(self)  # Return the string representation from __str__()

    def buy(self, quantity: int) -> float:
        if self.promotion:
            # Apply promotion if exists
            total_price = self.promotion.apply_promotion(self, quantity)
            self.quantity -= quantity  # Reduce stock based on quantity
            return total_price
        else:
            if quantity > self.quantity:
                raise ValueError("Not enough stock")
            self.quantity -= quantity  # Reduce stock
            return self.price * quantity


# class NonStockedProduct(Product):
#     def __init__(self, name: str, price: float):
#         super().__init__(name, price, quantity=0)  # Non-stocked products have 0 quantity
#
#     def buy(self, quantity: int) -> float:
#         if quantity <= 0:
#             raise ValueError("Quantity to buy must be greater than zero")
#         total_price = quantity * self.price
#         return total_price  # No need to reduce stock since it's non-stocked
#
#     def show(self) -> str:
#         return f"{self.name}, Price: {self.price} (Non-stocked product)"
#
#     def set_quantity(self, quantity: int):
#         raise ValueError("Cannot set quantity for non-stocked products.")
#
#     def is_active(self) -> bool:
#         return True  # Non-stocked products are always considered active


class NonStockedProduct(Product):
    def __init__(self, name: str, price: float):
        super().__init__(name, price, quantity=0)  # Non-stocked products have 0 quantity

    def buy(self, quantity: int) -> float:
        if quantity <= 0:
            raise ValueError("Quantity to buy must be greater than zero")
        total_price = quantity * self.price
        return total_price  # No need to reduce stock since it's non-stocked

    def show(self) -> str:
        return f"{self.name}, Price: {self.price} (Non-stocked product)"

    def set_quantity(self, quantity: int):
        raise ValueError("Cannot set quantity for non-stocked products.")

    def is_active(self) -> bool:
        return True  # Non-stocked products are always considered active


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

