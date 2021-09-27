# Week 3
# Chapter 3: Control Statements
# In-Class Examples

# If statements

keyDetected = False
if keyDetected:``
    print("I am in the if statement.")


age = 25
if age > 19:
    print("You may enter.")

age = 19
id_expired = True
if age >= 19 and not id_expired:
    print("You may enter.")
else:
    print("You may NOT enter.")


if age >= 19 and not id_expired:
    print("You may enter.")
elif age >= 19 and id_expired:
    print("Your id is expired. I cannot let you in.")
else:
    print("You may NOT enter.")


if age >= 19 and not id_expired:
    print("You may enter.")
else:
    if id_expired:
        print("Your id is expired.")
    print("You may NOT enter.")


#name = "john"
name = input("Enter your login name: ")
if name == "John":
    print("Hi, John!")
elif name == "Marianne":
    print("Hi, Marianne!")
elif name == "Sam":
    print("Hi, Sam!")
else:
    print("I don't know who you are!")


