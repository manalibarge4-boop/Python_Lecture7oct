#Print sum of first 10 even numbers
total = 0
for i in range(2, 21, 2):
    total = total + i
print("Sum of firts 10 even numbers is:", total)

#Accept Two values S and N. Print square of first N numbers starting from S
s = int(input("Enter starting numbers: "))
n = int(input("Enter how many numbers: "))
for i in range(s, n + s):
    print(i ** 2)

#Reverse the accepted string
s = input("Enter the string: ")
reverse_string = s[::-1]
print(reverse_string)

#Accept sentence from user and count the vowels
sentence = input("Enter sentence: ")
count = 0
for i in sentence.lower():
    if i in "aeiou":
        count = count + 1
print("Number of vowels:", count) 

#Remove duplicates from list
numbers = [1, 2, 3, 4, 2, 1, 3, 5]
unique_numbers= list(set(numbers))
print(unique_numbers)

#Reverse the list

numbers = [1, 2, 3, 4, 5]
numbers.reverse()
print(numbers)
