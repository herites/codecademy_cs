def main():
    hairstyles = [
        "bouffant",
        "pixie",
        "dreadlocks",
        "crew",
        "bowl",
        "bob",
        "mohawk",
        "flattop",
    ]
    prices = [30, 25, 40, 20, 20, 35, 50, 35]
    last_week = [2, 3, 5, 8, 4, 4, 6, 2]
    total_price = 0
    for price in prices:
        total_price += price
    average_price = total_price / len(prices)
    print(f"Average Haircut Price: {average_price}")
    new_prices = [x - 5 for x in prices]
    print(new_prices)
    total_revenue = 0
    for index, value in enumerate(prices):
        total_revenue += value * last_week[index]
    print(total_revenue)
    average_daily_revenue = total_revenue / 7
    print(average_daily_revenue)
    # range(len(hairstyles)) generates the index for the loop
    cuts_under_30 = [
        hairstyles[i] for i in range(len(hairstyles)) if new_prices[i] < 30
    ]
    print(cuts_under_30)


if __name__ == "__main__":
    main()
