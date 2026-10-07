#Python example for common function
"""
#simple string
text = " Welcome to IMCC  "

#1 strips spaces from both ends
print("Remove Spaces", text.strip())

#2 Convert to lower case
print("Lower Case :", text.lower())

#3 Convert to upper case
print("Upper Case :", text.upper())

#4 Capitalize first letter
text = text.strip()
print("Capitalize First letter: ", text.capitalize())

#5 Title case (Capitalize each word)
print(text.title())

#6 Count occurances of substring
print(" Letter C occurs ", text.count("c"), "times in text")

#7 Find the position of substring (-1 if not found)
print("Position of IMCC in text is ", text.find("IMCC"))

#8 Replace a substring
print(text.replace("IMCC", "Python Magic"))

#9 Check if string starts or ends with certain substring
print(text.startwith(" We"))
print(text.endswith("! "))

#10 Split string into List by a delimeter
print("Simple split", text.split())

#11 Join a list of strings with a separator
words = ["Python", "is", "fun"]
print(" ".join(words))

#Count the vowels 
alphabets = 

#Print Ha 3 times
txt = "ha"
print(txt*3)
"""
#name find the occurances of letter a in your name
name = "manali"
print(" Letter a occurs ", name.count("a"), "times in text")

#Replace your name with z
print(name.replace("a", "z"))

#Split your name in two parts 

#sorting
print(sorted(name)) #returns the list of characters in alphabetical way