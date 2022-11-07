selfName = "name"

selfAge = 19

selfCity = "city"

otherName = "name"

otherAge = 20

otherCity = "city"


#a
print(selfName == otherName or selfAge == otherAge or selfCity == otherCity)

#b
print(selfCity == otherCity and selfCity == "Castellon")

#c
print(selfCity == otherCity and selfCity != "Castellon")

#d
print(otherCity == "Castellon" or otherCity == "Valencia" or otherCity == "Alicante")

#e
print(not (otherCity == "Castellon" or otherCity == "Valencia" or otherCity == "Alicante"))

print(otherCity != "Castellon" and otherCity != "Valencia" and otherCity != "Alicante")

#f
print(selfAge // 10 == otherAge // 10);



