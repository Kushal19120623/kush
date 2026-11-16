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