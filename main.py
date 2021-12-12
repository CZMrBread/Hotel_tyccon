from classes.Colors import bcolors
from classes.Hotel import Hotel, room_names, room_option, furniture_names, furniture_option

inventory = []
rooms = []

hotel = Hotel(rooms, inventory, 10000)


def num_input():
    choice = input("Choose option: ")
    try:
        choice = int(choice) - 1
        if choice < 0:
            print(f"{bcolors.FAIL}{bcolors.BOLD}Wrong input!{bcolors.ENDC}")
            return "fail"
        return choice
    except ValueError:
        print(f"{bcolors.FAIL}{bcolors.BOLD}Wrong input!{bcolors.ENDC}")
        return "fail"


def shop():
    shopping = True
    while shopping:
        hotel.get_money()
        hotel.show_buy_option()
        choice = input("Choose option: ").lower()
        match choice:
            case "1" | "go back":
                shopping = False
            case "2" | "room":
                hotel.show_buy(room_option)
                choice = num_input()
                if choice == "fail":
                    continue
                elif choice >= len(room_names):
                    print(f"{bcolors.BOLD}{bcolors.FAIL}Input out of range!{bcolors.ENDC}")
                    continue
                chosen_room = room_names[choice]
                hotel.buy(chosen_room, room_option)
                if hotel.buy == "fail":
                    continue
                print([room.name for room in rooms])
            case "3" | "furniture":
                hotel.show_buy(furniture_option)
                choice = num_input()
                if choice == "fail":
                    continue
                elif choice >= len(furniture_names):
                    print(f"{bcolors.BOLD}{bcolors.FAIL}Input out of range!{bcolors.ENDC}")
                    continue
                chosen_furniture = furniture_names[choice]
                hotel.buy(chosen_furniture, furniture_option)
                if hotel.buy == "fail":
                    continue
                print([item.name for item in inventory])
            case _:
                print(f"{bcolors.FAIL}{bcolors.BOLD}Wrong input!{bcolors.ENDC}")
                continue


def room_management():
    manage = True
    options = ["Go back", "Equip", "Unequip", "Status"]
    while manage:
        i = 1
        for option in options:
            print(f"{i}. {option}")
            i += 1
        choice = input("Choose option: ").lower()
        match choice:
            case "1" | "go back":
                manage = False
            case "2" | "equip":
                pass
            case "3" | "unequip":
                pass
            case "4" | "status":
                pass
            case _:
                print(f"{bcolors.FAIL}{bcolors.BOLD}Wrong input!{bcolors.ENDC}")


def main():
    while True:
        actions = ["Shop", "Manage rooms"]
        for i, action in enumerate(actions, 1):
            print(f"{i}. {action}")
        choice = input("Choose option: ").lower()
        match choice:
            case "1" | "shop":
                shop()
            case "2" | "manage rooms":
                room_management()
            case _:
                print(f"{bcolors.FAIL}{bcolors.BOLD}Wrong input!{bcolors.ENDC}")
                continue


main()
