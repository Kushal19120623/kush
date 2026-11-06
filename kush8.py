#if else if condition
k=int(input("Enter a number: "))

if k%2==0:
    print("The number is even")
        
else:
    print("The number is odd")

attendance_percentage=int(input("Enter your attendance percentage: "))
if attendance_percentage>=75:
    print("You are allowed to sit in the exam")
elif attendance_percentage<75 and attendance_percentage>=60:
    print("You are allowed to sit in the exam with permission")
else:
    print("You are not allowed to sit in the exam")    
        
gender=input("Enter your gender (M/F): ")
age=int(input("Enter your age: "))
if gender=="f" and age<=5:
    print("You are a girl and you are a child and you have free ticket")
elif  5<age<=15:
    print("you are a teenager and you have half ticket")
elif age>60:
    print("You are a senior citizen and you have senior citizen discount")
elif gender=="m" and age>=18:
    print("You are a man and you have to pay full ticket")
else:
    print("invalid input")

#insert the card
pin=1234
card_trail=input("enter the pin: ")
if card_trail==pin:
    print("enter the amount: ")
else:
    print("passward is incorrect")


