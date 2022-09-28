#introduction of lists in python
primes=[2,3,5,7]
my_favorite_thing = [13,"bike"]
""" what is my favorite thing?"""
print (my_favorite_thing)
planets = ["Mercury","venus","Earth","Mars", "Jupiter","Saturn", "Uranus","Neptune"]
planets[5] = "Moon" # structure when you want to change value in list.
print(planets)
print(planets [0])
print(planets[1:4])
print(planets.index("venus"))
planets.sort()
print(planets)

#List fucntions
lucky_numbers = [3,7,10,13,23,69]
months = ["January", "Febuary", "March", "April", "May","June", "Juli", "August","September","October","November", "December"]
months.extend(lucky_numbers) #combine a new variabel into lists
print(months)
months.append("Rain")#to add new thing on lists
print (months)
months.insert(1,"Hot")# another way to enter new variable onto lists
print(months)
months.remove("Hot")# it's use to remove variable in list
print(months)

lucky_numbers2= lucky_numbers.copy()
print(lucky_numbers2)

