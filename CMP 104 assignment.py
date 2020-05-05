# Area of a square
L = int(input("Enter the value of the Length here: "))
A = L*L
print ("The answer is = ",A)

# Area of a rectangle
L = int(input("Enter the value of the Length here: "))
B = int(input("Enter the value of the Breadth here: "))
A = B*L
print("the answer is = ",A)

# Area of a triangle
b = int(input("Enter the value of the base here: "))
h = int(input("Enter the value of the height here: "))
A = 1/2*b*h
print("The answer is = ",A)

# Area of a trapeziod
h = int(input("Enter the value of the height here: "))
b1 = int(input("Enter the value of base 1 here: "))
b2 = int(input("Enter the value of base 2 here: "))
A = 1/2*(b1 + b2)*h
print("The answer is = ",A)

# Area of a circle
r = int(input("Enter the value of the radius here: "))
pi = 22/7
A = 2*pi**2
print("The answer is = ",A)

# Area of the circumference of a circle
r = int(input("Enter the value of the radius here: "))
pi = 22/7
A = 2*pi*r
print("The answer is = ",A)

# Area of a cube
a = int(input("Enter the value of the Length here: "))
A = 6*L**2
print("The answer is = ",A)

# Area of a cylinder
r = int(input("Enter the value of the Radius here: "))
h = int(input("Enter the value of the Height here: "))
pi = 22/7
A = 2*pi*r*h
print("The answer is = ",A)

# Total surface area of a cylinder
r = int(input("Enter the value of the Radius here: "))
H = int(input("Enter the value of the Height here: "))
pi = 22/7
A = 2*pi*r*(r*h)
print("The answer is = ",A)

# Volume of a cylinder
r = int(input("Enter the value of the Radius here: "))
h = int(input("Enter the value of the Height here: "))
pi = 22/7
V = pi*r**2*h
print("The answer is = ",V)

# Acceleration formula
v = int(input("Enter the value of the Final velocity here: "))
U = int(input("Enter the value of the Initial velocity here: "))
T = int(input("Enter the value of the Time here: "))
a = (V-U)/T
print("The answer is = ",a)

# Formula for density
m = int(input("Enter the value of the Mass here: "))
v = int(input("Enter the value of the Volume here:"))
P = m/v
print("The answer is = ",P)

# Formula for pressure
F = int(input("Enter the value of the force applied: "))
A = int(input("Enter the value of the Total area of the object: "))
P = F/A
print("The answer is = ",P)

# Formula for Kinetic energy
M = int(input("Enter the value of the mass here: "))
V = int(input("Enter the value of the Velocity here: "))
E = 1/2*M*V**2
print("The answer is =",E)

# Formula for voltage
I = int(input("Enter the value of the current here: "))
R = int(input("Enter the value of the Resistance in ohms here: "))
V = I*R
print("The answer is = ",V)