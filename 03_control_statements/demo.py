# age(variable)=12(value)
# Conditional Statements
# if Syntax
# if condition:
#     statement

if True:
    print("correct indentation")
    
#if syntax incorrect indentation
# if True:
# print("incorrect indentation") #  IndentationError: expected an indented block afteer 'if' statement on line 7

if 5<2:
    print("valid condition")
    
# if else
if 5<2:
    print("valid condition")
else:
    print("invalid condition")
    
if 5>2 and 5>3:
    print("valid condition")
else:
    print("invalid condition")


# voting app
age=12
if age>=18:
    print("you can vote")
else:
    print("you cannot vote")

#user input() -> for taking input from user
# dynamic voting app        
age = int(input("enter age of the person:"))
if age >= 18:
    print("you can vote")
else: 
    print("you cannot vote")
    

value = input("enter some value")
print(value)
print(type(value))


# ternary operator / conditional operator(short hand if-else statements)
age = int(input("enter value"))
status = "you can vote" if age>=18 else "you cannot vote"
print(status)

# elif for multiple conditions
marks = int(input("enter your marks:"))
if marks >= 90:
    print("A Grade")
elif marks >= 75:
    print("B Grade")
elif marks >= 60:
    print("C Grade")
elif marks >= 50:
    print("D Grade")
elif marks >= 35:
    print("E Grade")
else:
    print("Fail")

# Match Cases (switch case in java)
# this is introduced in python 3.1 onwards
choice = int(input("enter your choice (1-5):"))
match choice:
    case 1:
        print("Python")
    case 2:
        print("Java")
    case 3:
        print("C#")
    case 4:
        print("Cloud")
    case 5:
        print("DevOps")
    case _:
        print("give valid number between (1-5)")


# elif ladder 
age = 22
if age == 0 or age == 1 or age == 2 or age == 3 or age == 4:
    category = "Toddler"
elif age == 5 or age == 6 or age == 7 or age == 8 or age == 9 or age == 10 or age == 11 or age == 12:
    category = "child"
elif age == 13 or age == 14 or age == 15 or age == 16 or age == 17 or age == 18 or age == 19:
    category = "Teenager"
elif age == 20 or age == 21 or age == 22 or age == 23 or age == 24 or age == 25 or age == 26:
    category = "Young Adult"
else:
    category = "Adult"
print(age)
print(category)

# Match case
age = 22
match age:
    case 0 | 1 | 2 | 3 | 4:
        category = "Toddler"
    case 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12:
        category = "child"
    case 13 | 14 | 15 | 16 | 17 | 18 | 19:
        category = "Teenager"
    case 20 | 21 | 22 | 23 | 24 | 25 | 26:
        category = "Young Adult"
    case _:
        category = "Adult"
print(category)


