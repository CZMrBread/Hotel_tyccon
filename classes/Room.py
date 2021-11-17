class Room:
	def __init__(self, name, size, furniture, windows, balcony, price):
		self.name = name
		self.size = size
		self.space = size
		self.score = 0
		self.furniture = furniture
		self.windows = windows
		self.balcony = balcony
		self.price = price

	def get_free_space(self):
		return self.space

	def get_name(self):
		return self.name

	def get_size(self):
		return self.size

	def get_furniture(self):
		return self.furniture

	def print_furniture(self):
		i = 1
		print(self.name)
		for item in self.furniture:
			print("		" + str(i) + ".",
				  "Name:", item["name"].name,
				  "Size:", item["name"].size)
			i += 1

	def get_windows(self):
		return self.windows

	def get_balcony(self):
		return self.balcony

	def get_score(self):
		return self.score

	def get_price(self):
		return self.price

	def equip(self, equipment, inventory):
		self.space -= equipment["name"].size
		self.furniture.append(equipment)
		inventory.remove(equipment)

	def unequip(self, equipment, inventory):
		self.space += equipment["name"].size
		inventory.append(equipment)
		self.furniture.remove(equipment)

	def get_stats(self):
		print(f"Name: {self.name} │ "
			  f"Price: {self.price} │ "
			  f"Furniture {self.furniture} │ "
			  f"Space: {self.space}/{self.size}")
