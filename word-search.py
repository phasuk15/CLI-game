print("Welcome to Word Search!")

level = input("Choose your difficulty (easy, medium, hard): ");
animals = ["CAT", "DOG", "LION", "TIGER", "BEAR", "WOLF", "FOX", "DEER", "MOUSE", "HORSE"]
fruits = ["APPLE", "MANGO", "PEAR", "GRAPE", "KIWI", "LEMON", "BANANA", "ORANGE", "PLUM", "CHERRY"]
colors = ["RED", "BLUE", "GREEN", "YELLOW", "PURPLE", "ORANGE", "BLACK", "WHITE", "PINK", "BROWN"]
tech = ["PYTHON", "JAVA", "HTML", "CSS", "NODE", "SQL", "RUBY", "CPLUSPLUS", "JAVASCRIPT", "API"]
fun = ["SUN", "MOON", "STAR", "SKY", "RAIN", "SNOW", "TREE", "FIRE", "WATER", "ROCK"]


def gen_grid(number):
    grid = [[0 for x in range(number)] for y in range(number)]
    return grid


if level == "easy":
    grid = gen_grid(10)
    


elif level == "medium":
    grid = gen_grid(12)


else:
    grid = gen_grid(15)



