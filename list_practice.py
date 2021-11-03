cities = [
    "Oakland",
    "Atlanta",
    "New York City", 
    "Seattle",
    "Memphis",
    "Miami",
    "Boston",
    "Los Angeles",
    "Denver",
    "New Orleans",
]
print(cities)

lol_champs = [
    "Nasus",
    "Darius",
    "Lulu",
    "Ezreal",
    "Lissandra",
    "Shaco",
    "Caitlyn",
    "Twitch",
    "Kaisa",
    "Sona",
]
print(lol_champs)

print((cities)[1], cities[-3], cities[4])
print((lol_champs)[1], lol_champs[2], lol_champs[4])

first_four_cities = cities[0:4]
print(first_four_cities)

last_four_champs = lol_champs[-5:-1]
print(last_four_champs)

cities[0] = "San Francisco"
cities[2] = "Brooklyn"
cities[-3] = "Hollywood"
cities[-5] = "Tampa"
print(cities)

cities.append("Oakland")
cities.extend(["New York City", "Los Angeles"])
cities.insert(0, "Miami")
print(cities)

del cities[0]
print(cities)

cities.pop(-1)
print(cities)

cities.remove("Tampa")
print(cities)


