groceries = {
    "chicken":1.59,
    "beef":1.99,
    "cheese":1.00,
    "milk":2.50
    }

wowmounts = {
    "groundmountslow":20,
    "groundmountfast":40,
    "flymountfast":60,
    "flymountfaster":80,
    "flymountfastest":90
    }
chicken_price = groceries["chicken"]
beef_price = groceries["beef"]
cheese_price = groceries["cheese"]
milk_price = groceries["milk"]

groundmountslow_level = wowmounts["groundmountslow"]
groundmountfast_level = wowmounts["groundmountfast"]
flymountfast_level = wowmounts["flymountfast"]
flymountfaster_level = wowmounts["flymountfaster"]
flymountfastest_level = wowmounts["flymountfastest"]

shoe_inv = {
    "Jordan 13" : 1,
    "Yeezy" : 8,
    "Foamposite" : 10,
    "Air Max" : 5,
    "SB Dunk" : 20,
}

print(shoe_inv)

shoe_inv["SB Dunk"] -= 2
shoe_inv["Yeezy"] -= 1
shoe_inv["Jordan 13"] += 7
shoe_inv["Yeezy"] += 7
shoe_inv["Air Max"] += 7
shoe_inv["Foamposite"] += 7
shoe_inv["Jordan 13"] -= 3
shoe_inv["Yeezy"] -= 3
shoe_inv["Air Max"] -= 3
shoe_inv["Foamposite"] -= 3

print(shoe_inv)

groceries["eggs"] = 1.79
groceries["bacon"] = 1.89
groceries["soda"] = 1.39
print(groceries)

wowmounts["warbear"] = 40
wowmounts["drake"] = 80
wowmounts["raptor"] = 20
print(wowmounts)

shoe_inv["Jordan 11"] = 12
shoe_inv["Hiraches"] = 4
shoe_inv["Pumas"] = 2
print(shoe_inv)

del groceries["eggs"]
del groceries["bacon"]
print(groceries)

del wowmounts["warbear"]
del wowmounts["drake"]
print(wowmounts)

del shoe_inv["Jordan 11"]
del shoe_inv["Pumas"]
print(shoe_inv)

