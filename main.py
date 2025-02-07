# main.py
import store
import products

# Initialize product list
product_list = [
    products.Product("MacBook Air M2", price=1450, quantity=100),
    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
    products.Product("Google Pixel 7", price=500, quantity=250),
    products.NonStockedProduct("Windows License", price=125),
    products.LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
]

# Create promotion catalog
second_half_price = products.SecondHalfPrice("Second Half price!")
third_one_free = products.ThirdOneFree("Third One Free!")
thirty_percent = products.PercentDiscount("30% off!", percent=30)

# Add promotions to products
product_list[0].set_promotion(second_half_price)  # MacBook Air M2 gets second-half-price promotion
product_list[1].set_promotion(third_one_free)  # Bose earbuds get third one free promotion
product_list[3].set_promotion(thirty_percent)  # Windows license gets 30% discount

# Test buying products with promotions
for product in product_list:
    print(product.show())  # Show product info, including promotion if exists

    # Example buying quantities
    try:
        quantity_to_buy = 2 if isinstance(product, products.Product) else 1  # Adjust quantity for testing
        total_price = product.buy(quantity_to_buy)
        print(f"Total price for {quantity_to_buy} of {product.name}: ${total_price}")
    except ValueError as e:
        print(f"Error buying {product.name}: {e}")
    print()  # Add a line break between product tests


#
#
# # Setup initial stock of inventory
# product_list = [
#     products.Product("MacBook Air M2", price=1450, quantity=100),
#     products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
#     products.Product("Google Pixel 7", price=500, quantity=250),
#     products.NonStockedProduct("Windows License", price=125),  # Non-stocked product
#     products.Product("Shipping", price=10, quantity=250)  # Example limited product
# ]
#
# # Create promotion catalog
# second_half_price = products.SecondHalfPrice("Second Half price!")
# third_one_free = products.ThirdOneFree("Third One Free!")
# thirty_percent = products.PercentDiscount("30% off!", percent=30)
#
# # Add promotions to products
# product_list[0].set_promotion(second_half_price)
# product_list[1].set_promotion(third_one_free)
# product_list[3].set_promotion(thirty_percent)
#
#
#
# # # Setup initial stock of inventory
# # product_list = [
# #     products.Product("MacBook Air M2", price=1450, quantity=100),
# #     products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
# #     products.Product("Google Pixel 7", price=500, quantity=250),
# #     products.NonStockedProduct("Windows License", price=125),
# #     products.LimitedProduct("Shipping", price=10, quantity=250, maximum=1)
# # ]

best_buy = store.Store(product_list)


def list_all_products():
    """Lists all active products in the store."""
    products = best_buy.get_all_products()
    for product in products:
        print(product)


def show_total_amount():
    """Displays the total quantity of all products in store."""
    print(f"Total amount in store: {best_buy.get_total_quantity()} items.")


def make_an_order():
    """Allows the user to order products."""
    shopping_list = []
    while True:
        print("\nEnter product number to buy (or type 'done' to finish):")
        products = best_buy.get_all_products()

        for i, product in enumerate(products, 1):
            print(f"{i}. {product}")

        choice = input("Your choice: ").strip()
        if choice.lower() == "done":
            break

        try:
            index = int(choice) - 1
            if 0 <= index < len(products):
                quantity = int(input(f"Enter quantity for {products[index].name}: "))
                shopping_list.append((products[index], quantity))
            else:
                print("Invalid product number. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    if shopping_list:
        try:
            total_price = best_buy.order(shopping_list)
            print(f"Order placed successfully! Total cost: ${total_price:.2f}")
        except ValueError as e:
            print(f"Order failed: {e}")


def start():
    """Displays menu and handles user input."""
    menu = [
        "1. List all products in store",
        "2. Show total amount in store",
        "3. Make an order",
        "4. Quit"
    ]

    dispatch = {
        "1": list_all_products,
        "2": show_total_amount,
        "3": make_an_order,
        "4": exit
    }

    while True:
        print("\n" + "-" * 30)
        for option in menu:
            print(option)

        choice = input("Select an option: ").strip()
        if choice in dispatch:
            dispatch[choice]()
        else:
            print("Invalid choice, please try again.")


def main():
    print("Welcome to Best Buy!")
    start()


if __name__ == "__main__":
    main()

