n = int(input("Enter the number of rows and columns you want in triangle: "))

# Function to print upper triangle
def upper_triangle(n):
    for i in range(n):
        for j in range(n):
            if i <= j:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

# Function to print lower triangle
def lower_triangle(n):
    for i in range(n):
        for j in range(n):
            if i >= j:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()

# Function to print centered pyramid

def pyramid(s):
   # number of spaces
   x = s - 1
   for i in range(s):
      for j in range(x):
         print(end=" ")
      # decrementing x after each loop
      x = x - 1
      for j in range(i+1):
         # printing stars
         print("* ", end="")
      print("\r")



# Calling the functions
upper_triangle(n)
lower_triangle(n)
pyramid(n)
