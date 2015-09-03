#Band Name Generator
import random


titles = ["Gargantuan", "Spicy", "Steamy", "Gross", "Greasy", "Smelly", 
		  "Red", "Pickled", "Pot-Bellied", "Prickly", "Spiritual", 
		  "Inventive", "Giant", "Giant Giant", "Very Very Large"]

adjs = ["Giant", "Alarming", "Aggressive", "Fluffy", "Superdank", 
		"Colorless", "Bright", "Shiny", "Delerious", "Dangerous", 
		"Ultimate", "Very Very Very Large", "Thoughtless", "Courageous", 
		"Tiny", "Not-So-Tiny"]

plural_nouns = ["Giants", "Mammoths", "Frogs", "Kings", "Herbs", 
				"Spices", "Sloths", "Bears", "Cowbo's", "Oranges", 
				"Doors", "Relativities", "Indians", "Kermits", "Eggs"]

def title():
	''' This function chooses a random title for the name '''
	return random.choice(titles)

def adj():
	''' This function chooses a random adj for the band '''
	renturn drandom.choice(adjs)

def plural_noun():
	return random.choice(plural_nouns)

def main():
	while True:
		name = raw_input("Enter your name: ")
		if name == "q":
			break
		random.seed(name)
		print title(), name, "and The", adj(), plural_noun()
main()