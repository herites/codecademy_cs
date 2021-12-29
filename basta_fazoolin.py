class Menu:
    def __init__(self, name, items, start_time, end_time) -> None:
        self.name = name
        self.items = items
        self.start_time = start_time
        self.end_time = end_time

    def __repr__(self) -> str:
        return f"{self.name}, available from {self.start_time} to {self.end_time}"

    def calculate_bill(self, purchased_items):
        return sum(self.items[i] for i in purchased_items)


class Franchise:
    def __init__(self, address, menus) -> None:
        self.address = address
        self.menus = menus

    def __repr__(self) -> str:
        return f"{self.address}"

    def available_menus(self, time):
        available_menus = []
        for i in self.menus:
            if i.start_time <= time <= i.end_time:
                available_menus.append(i)
        return available_menus


class Business:
    def __init__(self, name, franchises) -> None:
        self.name = name
        self.franchises = franchises


def main():
    brunch = Menu(
        "Brunch",
        {
            "pancakes": 7.50,
            "waffles": 9.00,
            "burger": 11.00,
            "home fries": 4.50,
            "coffee": 1.50,
            "espresso": 3.00,
            "tea": 1.00,
            "mimosa": 10.50,
            "orange juice": 3.50,
        },
        11,
        16,
    )
    early_bird = Menu(
        "Early Bird Dinner",
        {
            "salumeria plate": 8.00,
            "salad and breadsticks (serves 2, no refills)": 14.00,
            "pizza with quattro formaggi": 9.00,
            "duck ragu": 17.50,
            "mushroom ravioli (vegan)": 13.50,
            "coffee": 1.50,
            "espresso": 3.00,
        },
        15,
        18,
    )
    dinner = Menu(
        "Dinner",
        {
            "crostini with eggplant caponata": 13.00,
            "ceaser salad": 16.00,
            "pizza with quattro formaggi": 11.00,
            "duck ragu": 19.50,
            "mushroom ravioli (vegan)": 13.50,
            "coffee": 2.00,
            "espresso": 3.00,
        },
        17,
        23,
    )
    kids = Menu(
        "Kids menu",
        {
            "chicken nuggets": 6.50,
            "fusilli with wild mushrooms": 12.00,
            "apple juice": 3.00,
        },
        11,
        21,
    )
    menu_list = [brunch, early_bird, dinner, kids]
    flagship_store = Franchise("1232 West End Road", menu_list)
    new_installment = Franchise("12 East Mulberry Street", menu_list)
    first_business = Business(
        "Basta Fazoolin' with my Heart", [flagship_store, new_installment]
    )
    arepas_menu = Menu(
        "Take a' Arepa",
        {
            "arepa pabellon": 7.00,
            "pernil arepa": 8.50,
            "guayanes arepa": 8.00,
            "jamon arepa": 7.50,
        },
        10,
        20,
    )
    arepas_place = Franchise("189 Fitzgerald Avenue", arepas_menu)
    arepa_business = Business("Take a' Arepa", arepas_place)


if __name__ == "__main__":
    main()
