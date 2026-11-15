<<<<<<< Updated upstream
#Task
#Given an integer, , perform the following conditional actions:
#
#If  is odd, print Weird
#If  is even and in the inclusive range of 2 to 5, print Not Weird
#If  is even and in the inclusive range of  6 to 20 , print Weird
#If  is even and greater than 20 , print Not Weird


if __name__ == '__main__':
    n = int(input().strip())
    if n%2!=0:
        print("Weird")
    elif n%2==0 and 2<n<5:
        print("Not Weird")
    elif n%2==0 and 6<n<20:
        print("Weird")
    elif n%2==0 and n>20:
        print("Not Weird")

#Task
#The provided code stub reads two integers from STDIN,  and . Add code to print three lines where:

#The first line contains the sum of the two numbers.
#The second line contains the difference of the two numbers (first - second).
#The third line contains the product of the two numbers.

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    

print(a+b)
print(a-b)
print(a*b)

#The provided code stub reads two integers,  and , from STDIN.

#Add logic to print two lines. The first line should contain the result of integer division,  // . The second line should contain the result of float division,  / .

#No rounding or formatting is necessary.
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a//b)
    print(a/b)

#The provided code stub reads an integer ,n , from STDIN. For all non-negative integers i<n , print i^2 .
if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        print(i**2)


#An extra day is added to the calendar almost every four years as February 29, and the day is called a leap day. It corrects the calendar for the fact that our planet takes approximately 365.25 days to orbit the sun. A leap year contains a leap day.
#In the Gregorian calendar, three conditions are used to identify leap years:
#The year can be evenly divided by 4, is a leap year, unless:
#The year can be evenly divided by 100, it is NOT a leap year, unless:
#The year is also evenly divisible by 400. Then it is a leap year.
#This means that in the Gregorian calendar, the years 2000 and 2400 are leap years, while 1800, 1900, 2100, 2200, 2300 and 2500 are NOT leap years. Source
#Task
#Given a year, determine whether it is a leap year. If it is a leap year, return the Boolean True, otherwise return False.
#Note that the code stub provided reads from STDIN and passes arguments to the is_leap function. It is only necessary to complete the is_leap function.

def is_leap(year):
    leap = False
    if year%100==0:
        print("its not a leap year" )
    elif year%4==0 and year%400==0:
        print("its a leap year")
    # Write your logic here
    
    return leap

year = int(input())
=======
#Task
#Given an integer, , perform the following conditional actions:
#
#If  is odd, print Weird
#If  is even and in the inclusive range of 2 to 5, print Not Weird
#If  is even and in the inclusive range of  6 to 20 , print Weird
#If  is even and greater than 20 , print Not Weird


if __name__ == '__main__':
    n = int(input().strip())
    if n%2!=0:
        print("Weird")
    elif n%2==0 and 2<n<5:
        print("Not Weird")
    elif n%2==0 and 6<n<20:
        print("Weird")
    elif n%2==0 and n>20:
        print("Not Weird")

#Task
#The provided code stub reads two integers from STDIN,  and . Add code to print three lines where:

#The first line contains the sum of the two numbers.
#The second line contains the difference of the two numbers (first - second).
#The third line contains the product of the two numbers.

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    

print(a+b)
print(a-b)
print(a*b)

#The provided code stub reads two integers,  and , from STDIN.

#Add logic to print two lines. The first line should contain the result of integer division,  // . The second line should contain the result of float division,  / .

#No rounding or formatting is necessary.
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(a//b)
    print(a/b)
>>>>>>> Stashed changes
