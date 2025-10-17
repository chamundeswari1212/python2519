import random
for i in range(3):
    otp=random.randint(1000,9999)
    print(otp)
    user_otp=int(input("enter otp: "))
    if user_otp == otp:
        print("Transaction Approved")
    else:
        print("Maximum Attemps Reached, try after 24 Hours")
