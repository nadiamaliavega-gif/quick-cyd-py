# a. Write a for loop that prints out "banana" one letter at a time, one letter per line
for letter in ("banana"):
    print (letter)
# b. Write a for loop that prints out "banana" backwards  one letter at a time, one letter per line
fruit = "banana"
for i in range(len(fruit) - 1, -1, -1):
    print(fruit[i])
# c. Copy your code that creates the seven dwarves list, write a for loop
#    that prints out each of the dwarves names
dwarves = ["Grumpy", "Happy","Sleepy","Sneezy","Dopey","Bashful","Doc"]
for i in range(len(dwarves)):
    print(dwarves[i])
# d. Write a for loop that prints each of the dwarf's names along with their
#    index in the list (0 - Sleepy, 1 - Happy...)
for i in range(len(dwarves)):
    print(i, "-", dwarves[i])

# e. Write a while loop that prints each of the dwarf's names along with their
#    index in the list (this should have the same output as the part c)
i = 0
while i <len(dwarves[i]):
    print(i,"-", dwarves[i])
    i = i + 1
# f. Using a while loop, repeatedly prompt the user to enter a positive number.
#    If the user enters a non-positive number, print an error and ask again.

# g. Using a while loop, implement a simple guessing game: pick a secret
#    number 1 to 100 and keep asking the user to guess until they get
#    it right; then print how many guesses it took.
