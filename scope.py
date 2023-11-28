# Scope - global and local

# a = 5
# b = [1, 2, 3]

fname = "Pat"
lname = "Cummins"

def greet():
    fname = "Steve"
    lname = "Smith"
    print("Inside Function")
    print(fname)
    print(lname)

print("Outside Function")
print(fname)
print(lname)
greet()