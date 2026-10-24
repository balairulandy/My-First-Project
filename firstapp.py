# This is a comment. The computer ignores lines starting with a hashtag.
print("Hello, world!")

name = input("What is your name? ")
print("Welcome to your first GitHub project, " + name + "!!")

# --- New: doubling a number 10 times ---
number = float(input("Enter a number: "))

for i in range(10):
    number = number * 2
    print("After doubling", i + 1, "time(s):", number)

print("Final result:", number)