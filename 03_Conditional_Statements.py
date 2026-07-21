print("------Conditional Statements")

print("--- if Statement ---")
# Running code only when a single condition is met.
weather = input("Is it raining today? (yes/no): ")

# We check if the user typed 'yes'
if weather == "yes":
    print("Take an umbrella with you!")
print("Notice: This line always prints, regardless of your input.\n")
print() # Blank line for spacing

print("---if-else statement---")
# Choosing between exactly two alternate paths (True or False).
user_age = int(input("Enter your age to check venue access: "))

if user_age >= 18:
    print("Access Granted: You are old enough to enter.")
else:
    print("Access Denied: You must be 18 or older.")
print()  # Blank line for spacing



print("--- if-elif-else statement ---")
#Evaluating multiple conditions in sequence.
traffic_light = input("Enter traffic light color (red/yellow/green): ")

if traffic_light == "red":
    print("STOP - Your vehicle must stop completely.")
elif traffic_light == "yellow":
    print("SLOW DOWN - Prepare to stop.")
elif traffic_light == "green":
    print("GO - It is safe to proceed.")
else:
    print("WARNING -The signal color is unknown.")
print("") # Blank line for spacing 


print("--- Nested Conditionals ---")
#Evaluating a secondary condition only after a primary condition passes.
username_input = input("Enter username: ").strip()

if username_input == "Monica":
    print("Username verified successfully.")
    
    # Nested if-else block inside the main 'if'
    # Python only reaches this point if the username matches 'Monica'
    password_input = input("Enter password: ")
    
    if password_input == "python123":
        print("Password matches. Login Successful!")
    else:
        print("Error - Incorrect password.")
else:
    print("Error - Username does not exist in our database.")
