def ground_shipping(weight):
    flat_rate = 20
    if weight <= 0:
        return print("Weight must be over 0")
    elif weight <= 2:
        price_per_pound = 1.5
        return {"ground shipping": ((price_per_pound * weight) + flat_rate)}
    elif weight <= 6:
        price_per_pound = 3.0
        return {"ground shipping": (price_per_pound * weight) + flat_rate}
    elif weight <= 10:
        price_per_pound = 4.00
        return {"ground shipping": (price_per_pound * weight) + flat_rate}
    else:
        price_per_pound = 4.75
        return {"ground shipping": (price_per_pound * weight) + flat_rate}


def ground_shipping_premium():
    return {"ground shipping premium": 125}


def drone_shipping(weight):
    if weight <= 0:
        return print("Weight must be over 0.")
    elif weight <= 2:
        price_per_pound = 4.5
        return {"drone shipping": price_per_pound * weight}
    elif weight <= 6:
        price_per_pound = 9
        return {"drone shipping": price_per_pound * weight}
    elif weight <= 10:
        price_per_pound = 12
        return {"drone shipping": price_per_pound * weight}
    else:
        price_per_pound = 4.75
        return {"drone shipping": price_per_pound * weight}


def shipping_fee_comparison(weight):
    # * unpacks iterables, ** unpacks dictionaries
    shipping_fees = {
        **ground_shipping(weight),
        **ground_shipping_premium(),
        **drone_shipping(weight),
    }
    # min() returns the lowest value, dict.get returns the key for that value
    # pass a function to the the key= argument
    cheapest_method = min(shipping_fees, key=shipping_fees.get)
    print(f"The cheapest shipping method is {cheapest_method}.")
    print(f"Price will be {shipping_fees[cheapest_method]} fabatka.")


def main():
    weight = input("Enter the weight of your package in pounds:\n")
    if weight.isnumeric() and float(weight) > 0:
        shipping_fee_comparison(float(weight))
    else:
        print("Please enter a number greater than zero.")


if __name__ == "__main__":
    main()
