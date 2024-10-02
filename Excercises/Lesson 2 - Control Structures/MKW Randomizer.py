import random

print("-= MKW Character/Vehicle Randomizer =-")
print("        -= By Riddim_GLiTCH =-        ")
print("Randomizing a Character and apropriate vehicle for you...")

weight=["light","medium","heavy"]

light_chars=["Baby Mario","Baby Luigi","Baby Peach","Baby Daisy","Toad","Toadette","Koopa Troopa","Dry Bones"]
med_chars=["Mario","Luigi","Princess Peach","Daisy","Yoshi","Birdo","Diddy Kong","Bowser Jr."]
heavy_chars=["Wario","Waluigi","Donkey Kong","Bowser","King Boo","Rosalina","Funky Kong","Dry Bowser"]

light_vehicles=["Standard Kart","Mini Beast","Tiny Titan","Blue Falcon","Cheep Charger","Booster Seat","Standard Bike","Magikruiser","Quacker","Jet Bubble","Bit Bike","Bullet Bike"]
med_vehicles=["Standard Kart","Sprinter","Daytripper","Wild Wing","Super Blooper","Classic Dragster","Standard Bike","Sugarscoot","Sneakster","Dolphin Dasher","Zip Zip","Mach Bike"]
heavy_vehicles=["Standard Kart","Offroader","Flame Flyer","Jetsetter","Honeycoupe","Piranha Prowler","Standard Bike","Wario Bike","Shooting Star","Flame Runner","Spear","Phantom"]

weight_class = random.choice(weight)

if weight_class == "light":
    char = random.choice(light_chars)
    vehicle = random.choice(light_vehicles)
elif weight_class == "medium":
    char = random.choice(med_chars)
    vehicle = random.choice(med_vehicles)
elif weight_class == "heavy":
    char = random.choice(heavy_chars)
    vehicle = random.choice(heavy_vehicles)

print("You will play the next race as",char,"on",vehicle)
input("Press Enter to confirm and exit...")