import shelve

#opens file
f = shelve.open("save.dat")
gold = 2
potions = "3"
#sets all variables as a dictionary
f["attributes"] = {"gold": gold, "potions": potions}
#f.sync() adds all any f["whatever"] to the file
f.sync()
#always close after use!!!
f.close()

#reopen file later to read the contents
f = shelve.open("save.dat")
#save the variables still in dictionary form to a new variable
attributes = f["attributes"]
#always close after use!!!
f.close()
#access each variable individually, and save them to a new variable to match the rest of your code.
gold = attributes["gold"]
print(gold)
