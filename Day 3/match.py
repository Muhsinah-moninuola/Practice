item = ("laptop", 250000)

match item:
    case ("phone", price):
        print(f"Phone with price: ₦{price}")
    case ("laptop", price):
        print(f"Laptop with price: ₦{price}")
    case (_, price) if price > 500000:
        print("Luxury item detected")
    case _:
        print("Unknown item")

fruit = ("banana", "ripe")

match fruit:
    case ("banana", "ripe"):
        print("Eat the banana 🍌")
    case ("banana", "unripe"):
        print("Let it ripen 🍃")
    case _:
        print("Unknown fruit")