
#Empty List
my_list = [] #lists are mutable
print(my_list)

#with Items
fruits = ["apple", "banana", " cherry"]
print(fruits)

#to access any elements use index
#positive number indicate from start negative number indicate from last nu,ber
#0 is first element and -1 is last element

number = [10, 20, 30, 40]
print(number[0])
print(number[-1])

#Append item in list
colors = ["red", "blue"]
colors.append("green")
print("After adding at last", colors)

#insert at specific location
colors.insert(1,"purple")
print(colors)



#Functions
#Length
numbers = [ 1, 2, 3, 4, 5, 6]
print("No. of items in list are", len(numbers))

#sum
print("Sum of the list numbers are", sum(numbers))

#sorting
print("list in ascending order", sorted(numbers))
print("list in descending order", sorted(numbers, reverse=True))

#Create a list of 10 numbers and display the sum of last four elements
#Remove the items from the list located at second and fifth position
#print the difference of highest and smallest number from the list
#append a new element in the list which is half of the item located third position in list

number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("The sum of last four element is: ", sum(number[-4:]))

print(number.pop(1))
print(number.pop(4))
print(number)

print(max(number))
print(min(number))
print("The difference of highest and smallest number from the list is: ", max(number) - min(number))

number.append(number[2] / 2)
print(number)