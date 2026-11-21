#You are given an integer,N
#  . Your task is to print an alphabet rangoli of size .
#  (Rangoli is a form of Indian folk art based on creation of patterns.
import string
def print_rangoli(size):
    alpha = string.ascii_lowercase
    lines = []

  # Calculate total width of each row
    width = 4 * size - 3

    for i in range(size):
        s = "-".join(alpha[i:size])
        row = (s[::-1] + s[1:]).center(width, "-")
        lines.append(row)
    print("\n".join(lines[::-1] + lines[1:]))

    
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)

#Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given  scores. Store them in a list and find the score of the runner-up
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    uni=sorted(set(arr))
    
    print(uni[-2])
    print()

#Let's learn about list comprehensions! You are given three integers  and  representing the dimensions of a cuboid along with an integer . Print a list of all possible coordinates given by  on a 3D grid where the sum of  is not equal to . Here, . Please use list comprehensions rather than multiple loops, as a learning exercise.
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    l=[[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k!=n ]
    print(l)

#The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students. Print the average of the marks array for the student name provided, showing 2 places after the decimal.
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
avr=sum(student_marks[query_name])/3
print("{:.2f}".format(avr))

