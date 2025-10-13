# Nested Conditions : condition inside condition
# dynamic voting app

age = int(input("enter Age:"))
has_id = input("do you have id (yes/no):")
if age >= 18:
    if has_id == "yes":
        print("you can vote")
    else:
        print("you need an id to vote")
else:
    print("you cannot vote / you are too young to vote")
    
    
