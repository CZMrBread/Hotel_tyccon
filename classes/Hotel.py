from classes.Colors import bcolors


class Hotel:
	def __init__(self, rooms, inventory, money):
		self.stars = 1
		self.rooms = rooms
		self.inventory = inventory
		self.money = money
		self.buy_options = ["Room", "Furniture"]

	def return_money(self):
		return self.money

	def get_money(self):
		if self.money >= 0:
			print(bcolors.OKGREEN + bcolors.BOLD + str(self.money) + "$" + bcolors.ENDC)
		else:
			print(bcolors.FAIL + bcolors.BOLD + str(self.money) + "$" + bcolors.ENDC)

	def add_money(self, amount):
		self.money += amount

	def sub_money(self, amount):
		self.money -= amount

	def get_stars(self):
		return self.stars

	def get_rooms(self):
		i = 1
		room_name = ""
		self.rooms.sort(key=lambda x: x["name"].name)
		print("Your rooms")
		for room in self.rooms:
			if room["name"].name == room_name:
				i += 1
				print(f"{i}. {room['name'].name} "
					  f"Price: {room['name'].price} ")
			else:
				i = 1
				room_name = room["name"].name
				print(bcolors.BOLD + bcolors.OKBLUE + "—" * 50 + bcolors.ENDC)
				print(f"{i}. {room['name'].name} "
					  f"Price: {room['name'].price} ")

	def get_inventory(self):
		i = 1
		item_name = ""
		self.inventory.sort(key=lambda x: x["name"].name)
		print("Your inventory")
		for item in self.inventory:
			if item["name"].name == item_name:
				i += 1
				print(f"{i}. {item['name'].name} "
					  f"Price: {item['name'].price} ")
			else:
				i = 1
				item_name = item["name"].name
				print(bcolors.BOLD + bcolors.OKBLUE + "—" * 50 + bcolors.ENDC)
				print(f"{i}. {item['name'].name} "
					  f"Price: {item['name'].price} ")


	def show_buy_options(self):
		i = 2
		print("1. Go back")
		for option in self.buy_options:
			print(f"{i}. {option}")
			i += 1

	def show_buy(self, buy):
		i = 1
		for item in buy:
			print(f"{i}. "
				  f"Name: {item['name'].name} "
				  f"Price: {item['name'].price} ")
			i += 1

	def buy(self, name, inventory, options):
		for item in options:
			if item["name"].name == name:
				if item["name"].price <= self.return_money():
					self.sub_money(item["name"].price)
					inventory.append(item)
					return "success"
				else:
					print(bcolors.FAIL + bcolors.BOLD + "Not enough money")
					return "fail"
