# Simple Python program for beginners

# Print a message
print("Guten Tag, Welt!")

# Get use input
name = input("What is your name?")

# Greet the use
print("Hello, " + name + "!")

# Simple math
number = int(input("Enter a number to square:"))
print("Your number squared is:", number ** 2)
# Simple conditional
if number > 10:
    print("That's a big number!")
    # Simple loop
    for i in range(1, number + 1):
        print(i, end=' ')
    else:
        print("\nLoop finished!")
        # Simple function
        def greet_user(name):
            return f"Hello, (name)! Welcome to the program. Enjoy your day!"
        # Call the function
        greeting = greet_user(name)
        print(greeting)
        #Simple list
        fruits = ["apple", "banana", "cherry"]
        print("here are some fruits:")
        for fruit in fruits:
            print(fruit)
            #Simple dictionary
            person = {
                "name": name, 
                "age": 47,
                "city": "Munich"
            }
            print("Person details:")
            for key, value in person.items():
                print(f"{key}: {value}")
                #End of the program
                print("Thank you for using the program!")
                print("Goodbye!")
                #End of the program
                exit()
                #End of the Program
                #This is a simple PYthon program for beginners
