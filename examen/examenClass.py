class House:# height, area, nOfWalls
	def __init__(self, _height, _area, _nOfWalls):
		self.height = _height
		self.area = _area
		self.nOfWalls = _nOfWalls
	def __str__(self):
		return "House with height: {0}, area: {1}, nOfWalls: {2}".format(self.height, self.area, self.nOfWalls)

	def Expand(self, heightIncrement, areaIncrement):
		self.height += heightIncrement
		self.area += areaIncrement

	def GetPrice(self):
		volume = self.area * self.height

		cost = volume + self.nOfWalls

		return cost

	def __add__(self, other):
		newHouse = House(self.height, self.area, self.nOfWalls);

		newHouse.Expand(other.height, other.area)

		newHouse.nOfWalls += other.nOfWalls

		return newHouse
	def __eq__(self, other):
		return self.height == other.height and self.area == other.area

	def __ne__(self, other):
		return self.height != other.height or self.area != other.area


	def __gt__(self, other):
		return self.GetPrice() > other.GetPrice()


#construction site

apartment = House(5, 25, 4)

villa = House(20, 120, 50)

print(villa)

apartment.Expand(30, 200)

print(apartment)

print("My house is bigger {0}".format(apartment > villa))
villa.Expand(1000, 10000)
print("My house is bigger {0}".format(apartment > villa))
