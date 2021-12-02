from classes.Hotel import Hotel
from classes.Room import Room
from classes.Furniture import Furniture
from classes.Colors import bcolors

small_bed = Furniture("Small bed", "bed", 3, 100, 2, 3, 0, 50)
large_bed = Furniture("Large bed", "bed", 3, 100, 4, 3, 0, 100)
small_wardrobe = Furniture("Small wardrobe", "wardrobe", 3, 100, 2, 3, 20, 7)

furniture_option = [{"name": small_bed},
                    {"name": large_bed},
                    {"name": small_wardrobe}]

small_room = Room("Small room", 10, [], 2, False, 2000)
large_room = Room("Large room", 20, [], 4, True, 3000)

room_option = [{"name": small_room},
               {"name": large_room}]

inventory = [{"name": small_bed}, {"name": small_bed}, {"name": small_bed}, {"name": small_wardrobe}]
rooms = [{"name": small_room}, {"name": large_room}, {"name": large_room}]

hotel = Hotel(rooms, inventory, 10000)


def num_input():
    choice = input("Choose option: ")
    try:
        choice = int(choice) - 1
        return choice
    except ValueError:
        print(f"{bcolors.FAIL}{bcolors.BOLD} Wrong input!{bcolors.ENDC}")
        return "fail"


def shop():
    shopping = True
    while shopping:
        hotel.get_money()
        hotel.show_buy_options()
        choice = input("Choose option: ").lower()
        match choice:
            case "1"|"go back":
                shopping = False
            case "2"|"room":
                hotel.show_buy(room_option)
                choice = num_input()
                if choice == "fail":
                    continue

                if choice >= len(room_option):
                    print(bcolors.FAIL + bcolors.BOLD + "Wrong input" + bcolors.ENDC)
                    continue

                flag = hotel.buy(room_option[choice]["name"].name, rooms, room_option)
                if flag == "fail":
                    continue
                else:
                    hotel.get_rooms()
                    print("\n")
            case "3"|"furniture":
                hotel.show_buy(furniture_option)
                choice = right_input()
                if choice == "fail":
                    continue

                if choice >= len(furniture_option):
                    print(bcolors.FAIL + bcolors.BOLD + "Wrong input" + bcolors.ENDC)
                    continue

                flag = hotel.buy(furniture_option[choice]["name"].name, inventory, furniture_option)
                if flag == "fail":
                    continue
                else:
                    hotel.get_inventory()
                    print("\n")
            case _:
                print(f"{bcolors.FAIL}{bcolors.BOLD}Wrong input!{bcolors.ENDC}")
                continue

def room_managment():
    manage = True
    options = ["Go back", "Equip", "Unequip", "Status"]
    while manage:
        i = 1
        for option in options:
            print(f"{i}. {option}")
            i += 1
        choice = input("Choose option: ").lower()
        match choice:
            case "1"|"go back":
                manage = False
            case "2"|"equip":
                for room in rooms:
                    room["name"].get_stats()
                choice = right_input()
                if choice >= len(rooms):
                    print(bcolors.FAIL + bcolors.BOLD + "Wrong input" + bcolors.ENDC)
                    continue
                if choice == "fail":
                    continue
                chosen_room = rooms[choice]
                hotel.get_inventory()
            case "3"|"unequip":
                pass
            case "4"|"status":
                pass
            case _:
                print(f"{bcolors.FAIL}{bcolors.BOLD}Wrong input!{bcolors.ENDC}")


while True:
    actions = ["Shop", "Manage rooms"]
    for i, action in enumerate(actions, 1):
        print(f"{i}. {action}")
    choice = input("Choose option: ").lower()
    match choice:
        case "1"|"shop":
            shop()
        case "2"|"manage rooms":
            room_managment()


"""
running = True
while running:

	hotel.get_money()
	hotel.show_buy_options()
	choice = right_input()
	if choice == "fail":
		continue

	if choice == 0:
		hotel.show_buy(room_option)
		choice = right_input()
		if choice == "fail":
			continue

		if choice >= len(room_option):
			print(bcolors.FAIL + bcolors.BOLD + "Wrong input" + bcolors.ENDC)
			continue

		flag = buy(room_option[choice]["name"].name, "room")
		if flag == "fail":
			continue

	elif choice == 1:
		hotel.show_buy(furniture_option)
		choice = right_input()
		if choice == "fail":
			continue

		if choice >= len(furniture_option):
			print(bcolors.FAIL + bcolors.BOLD + "Wrong input" + bcolors.ENDC)
			continue

		flag = buy(furniture_option[choice]["name"].name, "furniture")
		if flag == "fail":
			continue

	running = False
"""
