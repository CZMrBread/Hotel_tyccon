from classes.Hotel import Hotel
from classes.Room import Room
from classes.Furniture import Furniture
from classes.Colors import bcolors
import json

room_option = json.loads(open("room_prefab.json").read())
furniture_option = json.loads(open("furniture_prefab.json").read())

room_names = [room for room in room_option]
furniture_names = [furniture for furniture in furniture_option]
inventory = []
rooms = []

hotel = Hotel(rooms, inventory, 10000)


def show_buy(inventory):
    for i, item in enumerate(inventory, 1):
        print(f"{i}. {inventory[item]}")

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
                show_buy(room_option)
                choice = num_input()
                if choice == "fail":
                    continue
                elif choice >= len(room_names):
                    print(f"{bcolors.BOLD}{bcolors.FAIL}Input out of range!{bcolors.ENDC}")
                    continue
                chosen_room = room_names[choice]
                hotel.buy(chosen_room, room_option, True)
            case "3" | "furniture":
                show_buy(furniture_option)
                choice = num_input()
                if choice == "fail":
                    continue
                elif choice >= len(furniture_names):
                    print(f"{bcolors.BOLD}{bcolors.FAIL}Input out of range!{bcolors.ENDC}")
                    continue
                chosen_furniture = furniture_names[choice]
                hotel.buy(chosen_furniture, furniture_option, False)
                print(inventory)
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
                room_managment()
            case _:
                print(f"{bcolors.FAIL}{bcolors.BOLD}Wrong input!{bcolors.ENDC}")
                continue

main()