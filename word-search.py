import random
import string

print("Welcome to Word Search!")

level = input("Choose your difficulty (easy, medium, hard): ");

animals = ["CAT", "DOG", "LION", "TIGER", "BEAR", "WOLF", "FOX", "DEER", "MOUSE", "HORSE"]
fruits = ["APPLE", "MANGO", "PEAR", "GRAPE", "KIWI", "LEMON", "BANANA", "ORANGE", "PLUM", "CHERRY"]
colors = ["RED", "BLUE", "GREEN", "YELLOW", "PURPLE", "ORANGE", "BLACK", "WHITE", "PINK", "BROWN"]
tech = ["PYTHON", "JAVA", "HTML", "CSS", "NODE", "SQL", "RUBY", "CPLUSPLUS", "JAVASCRIPT", "API"]
nature = ["SUN", "MOON", "STAR", "SKY", "RAIN", "SNOW", "TREE", "FIRE", "WATER", "ROCK"]

direction = ["up", "down", "left", "right"]


def gen_grid(size):
    return [["_" for _ in range(size)] for _ in range(size)]

def populate(bank, size, grid):
    for word in bank:
        placed = False
        word_len =len(word)

        while not placed:
            x = random.randint(0, size - 1)
            y = random.randint(0, size - 1)

            dir = random.choice(direction)

            if dir == "up" and x - word_len + 1 >= 0:
                if all(grid[x - i][y] in ("_", word[i]) for i in range(word_len)):
                    for i in range(word_len):
                        grid[x - i][y] = word[i]
                    placed = True

            elif dir == "down" and x + word_len <= size:
                if all(grid[x + i][y] in ("_", word[i]) for i in range(word_len)):
                    for i in range(word_len):
                        grid[x + i][y] = word[i]
                    placed = True

            elif dir == "left" and y - word_len + 1 >= 0:
                if all(grid[x][y - i] in ("_", word[i]) for i in range(word_len)):
                    for i in range(word_len):
                        grid[x][y - i] = word[i]
                    placed = True

            elif dir == "right" and y + word_len <= size:
                if all(grid[x][y + i] in ("_", word[i]) for i in range(word_len)):
                    for i in range(word_len):
                        grid[x][y + i] = word[i]
                    placed = True
 
def fill_grid(grid):
    size = len(grid)
    for i in range(size):
        for j in range(size):
            if grid[i][j] == "_":
                grid[i][j] = random.choice(string.ascii_uppercase)

grid = gen_grid(10)
populate(animals, 10, grid)
fill_grid(grid)


def print_grid(grid):
    for row in grid:
        print(" ".join(row))


def play(level):
    if level == "easy":
        grid = gen_grid(10)
        populate(animals, 10, grid)
        fill_grid(grid)
        print_grid(grid)




    elif level == "medium":
        grid = gen_grid(12)
        populate(animals, 10, grid)
        fill_grid(grid)
        print_grid(grid)



    else:
        grid = gen_grid(15)
        populate(animals, 10, grid)
        fill_grid(grid)
        print_grid(grid)

