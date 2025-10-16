# looping statements

# While
# Syntax
# while condition:
    # code to repeat
    
count = 1
while count <= 5:
    print(count)
    count += 1


# Simulate real world use case for while
atm_correct_pin = 6534
user_given_pin = 6534
while user_given_pin != atm_correct_pin:
    print("incorrect pin please try again")
    user_given_pin = int(input("enter pin: "))
print("you can withdraw")


# Inifite loop
# count = 1
# while True:
    # print(count)
    # count += 1 # to stop loop "cltr+c"
    
# For loop : Used to Iterate over a sequence(Multiple)
# Syntax
# for elements in Sequenc:
    # statements
text = "Python is a general purpose programming language"
for i in text:
    print(i)
    
 
# num = 10
# for i in num:
    # print(i) # TypeError : 'int' object is not iterable

# Test to check given object is iterable
num = 10
print(type(int))
print(dir(num))

text = "Python"
print(type(text))
print(dir(text)) #it shows functionalities of variables

list_nums = [10,20,30]
print(type(list_nums))
print(dir(list_nums))
for num in list_nums:
    print(num)
    
print("="*50)
# For loop : Repeat block of code, if you know number of iterations in advance
# Range()
for i in range (10):
    print(i)

print("="*50)    
for i in range(10):
    print("Hi")





