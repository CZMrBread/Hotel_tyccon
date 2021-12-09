from classes.Colors import bcolors
from classes.Room import Room
from classes.Furniture import Furniture

class Hotel:
    def __init__(self, rooms, inventory, money):
        self.stars = 1
        self.rooms = rooms
        self.inventory = inventory
        self.money = money
        self.buy_options = ["Go back", "Room", "Furniture"]

    def return_money(self):
        return self.money

    def get_money(self):
        if self.money >= 0:
            print(f"{bcolors.OKGREEN}{bcolors.BOLD}{self.money}${bcolors.ENDC}")
        else:
            print(f"{bcolors.FAIL}{bcolors.BOLD}{self.money}${bcolors.ENDC}")

    def add_money(self, amount):
        self.money += amount

    def sub_money(self, amount):
        self.money -= amount

    def get_stars(self):
        return self.stars

    def get_room_stats(self):
        return

    def show_buy_option(self):
        for i, option in enumerate(self.buy_options, 1):
            print(f"{i}. {option}")

    def buy(self, item, prefab, room):
        if room:
            self.rooms.append(Room(prefab[item]["name"],
                                   prefab[item]["size"],
                                   prefab[item]["furniture"],
                                   prefab[item]["windows"],
                                   prefab[item]["balcony"],
                                   prefab[item]["price"]))
        elif not room:
            self.inventory.append(Furniture(prefab[item]["name"],
                                            prefab[item]["typ"],
                                            prefab[item]["quality"],
                                            prefab[item]["cleanliness"],
                                            prefab[item]["size"],
                                            prefab[item]["comfort"],
                                            prefab[item]["storage"],
                                            prefab[item]["price"]))