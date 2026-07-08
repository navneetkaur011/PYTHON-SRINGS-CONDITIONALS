# Write a program to input user's first name and print its length 
print("---Ques-01---")
Name = input("Enter your first name: ")
print("Length of your name is: ", len(Name))
print()

# Write a program to find the occurence of '$' in the string
print("---Ques-02---")
Text = """
        The cost of freshly brewed Caramel Frappuccino 
        ranges from $4.95 to $6.48, while a standard 
        cold coffee is around $3.75 to $4.95  
        """
print("Found $", Text.count("$"), "times in a string.")
print()

# Write a program to check if the number entered by the use is even or odd
print("---Ques-03---")
N = int(input("Enter your number: "))
if (N%2 == 0):
    print("EVEN")
else:
    print("ODD")
print()

# Write a prpgram to find the greatest of 3 numbers entered by the user 
print("---Ques-04---")
N1 = int(input("Enter first number: "))
N2 = int(input("Enter second number: "))
N3 = int(input("Enter third number: "))

if (N1>N2 and N1>N3):
    print("The gretest number is: " ,N1)
elif (N2>N1 and N2>N3):
    print("The gretest number is: " ,N2)
else:
    print("The gretest number is: " ,N3)
print()


# Write a program to check if the number is multiple of 7 or not
print("---Ques-05---") 
A = int(input("Enter a number: "))
if (A%7 == 0):
    print(A,"is a multiple of 7.")
else :
    print(A, "is not a multiple f 7.")
