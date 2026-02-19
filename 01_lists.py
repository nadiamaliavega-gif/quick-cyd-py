# Part 1 - the seven (or eight) dwarves
# a. Replace "None" on line 2 with a list that contains the names of the seven dwarves
# Grumpy, Happy, Sleepy, Sneezy, Dopey, Bashful, and Doc
dwarves = ["Grumpy", "Happy","Sleepy","Sneezy","Dopey","Bashful","Doc"]
# print("The seven dwarves: " + str(dwarves))
print("The seven dwarves: "+ str(dwarves))
# b. Join the crew! Write one line below that adds your name 
#write a line that prints the new list
dwarves.append("Nadia")
print(dwarves)
# c. There are two ways to print out your name from the list using indexes. Do them both
print(dwarves[7])
print(dwarves[-2])
# d. Uncomment the line below and print Happy's name using his index in the list
print(dwarves[1])
# e. Maybe eight is two many, write a line to remove a specific dwarf's name
# (this can be you or another dwarf)
dwarves.remove("Happy")
print(dwarves)
# f. Write one line of code below so that when the list is printed again it is
#    in alphabetical order
dwarves.sort()
# print("Seven alphabetical dwarves: " + str(dwarves))
print("Seven alphabetical dwarves: " + str(dwarves))
# Part 2 - counting
# a. create a variable named one_to_ten that contains the numbers 0 to 100
#    use the range function to do it without typing all the number yourself
one_to_ten = list(range(0,101))
print(one_to_ten)
# b. use the range function a variable named evens that contains even numbers
#    from 0 to 100 
evens = list(range(0,101,2))
print(evens)
#    hint: the range function's third parameter will help with this
#    https://www.w3schools.com/python/ref_func_range.asp
# c. use range to create a list that counts *backward* from one to 100
backwards = list(range(100,0,-1))
print(backwards)
# d. use range to create a list that counts *backward by 5* fromn 100
#    as in 100, 95, 90, 85, 80...
backward_from_5 = list(range(100,0,-5))
print(backward_from_5)