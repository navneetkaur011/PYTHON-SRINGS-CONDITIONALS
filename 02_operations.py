print("------01 BASIC OPERATIONS------")
# Concatenation - Joins two or more strings together.
str1 = "Pedro"
str2 = "and Pritam"
print(str1+" "+str2) 

# Repitition - Repeats a string a specified number of times
print("Hello " * 10) 

# Membership = Checks if substring exists inside the string
Line = "Pedro is a cop"
print("Pedro" in Line) # True 
print("Pedro" not in Line) #False
print()

print("------02 LENGTH OF STRING------")
str1 = "'Pedro and Pritam' is a nice series."
str2 = "Pedro is a crimebranch officer."
str3 = "Pritam is a salesperson and also a cyber expert."
print(len(str1))
print(len(str2))
print(len(str3))
print()

print("------INDEXING AND SLICING------")
# Indexing - Grabbing a single character
Text = "Python"
print(Text[0])
print(Text[5])
print()
# Slicing - Extracting a portion of a string.
text = "CrimeBranch"
print(text[0:5])  # Output: "Crime" (indices 0 to 4)
print(text[5:])   # Output: "Branch" (index 5 to the end)
print(text[::-1]) # Output: "hcnarBemirC" (reverses the string)
print()

print("------Common Built-in Methods------")
text = "PeDrO and prItAm"
print(text.upper())      # "PEDRO AND PRITAM"
print(text.lower())      # "pedro and pritam"
print(text.capitalize()) # "Pedro and pritam" (only capitalizes the very first letter)
print(text.title())      # "Pedro And Pritam" (capitalizes every word)
print(text.endswith("tam")) # false because ends with 'tAm' , not 'tam'
print(text.replace("r","l")) # PeDlO and plItAm
print(text.replace("PeDrO","Cop")) # Cop and prItAm
print(text.find("and")) # 6 (index)
print(text.find("Q")) # -1 (not a valid index)
print(text.count("r")) # 2 (as 'r' exist two times in the string)
