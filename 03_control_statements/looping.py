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

print("="*50)
for i in range (1,6):
    print(i)

print("="*50)
for num in range (1,10,1):
    print(num)

print("="*50)
for ij in range(1,10,2):
    print(ij)

print("="*50)
for i in range(10,1,-1):
    print(i)

# for i in range(1,10,1,4): # TypeError : range expected at most 3 arguments, got 4
    # print(i) 

print("="*50)

# get even numbers
print("printing even nums from 1 to 20")
num =2
while num <=20:
    print(num)
    num +=2

# loop with condition
num =2
while num <= 20:
    if num%2 ==0:
        print(num)
    num+= 1

print("="*50)
# get even numbers
print("printing even numbers 1 to 20:")
for i in range(2,22,2):
    print(i)
    


# List of courses
course_list = ["python","cloud","devops","ai"]
for course in course_list:
    print(course)


# Nested loops
for i in range(1,4):
    for j in range(1,4):
        print(f"{i} X {j} = {i*j}")
    print("------")
    
# Nested loops
i = 1
while i<4:
    j=1
    while j<4:
        print(f"{i} X {j} = {i*j}")
        j+=1
    print("-------")
    i+=1
    
# Branching statements
# break

for i in range(5):
    if i ==3:
        break # loop will stop here
    print(i)

# continue: skips the current iteration and continue the loop
for i in range(5):
    if i==3:
        continue # skip this current iteration
    print(i)

# pass: does nothing, generally used as place holder 
if 5>9:
    pass


print("="*25)
# pass : using for future
for num in range(5):
    if num==3:
        pass #keep future code here
    print(num)