

class Furniture:
	def __init__(self, name, typ, quality, cleanliness, size, comfort, storage, price):
		self.name = name
		self.typ = typ
		self.quality = quality
		self.cleanliness = cleanliness
		self.size = size
		self.comfort = comfort
		self.storage = storage
		self.price = price

	def get_name(self):
		return self.name

	def get_type(self):
		return self.typ

	def get_quality(self):
		return self.quality

	def get_cleanliness(self):
		return self.cleanliness

	def get_size(self):
		return self.size

	def get_comfort(self):
		return self.comfort

	def get_storage(self):
		return self.storage

	def get_price(self):
		return self.price

	def get_stats(self):