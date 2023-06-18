import numpy as np

# a*x + b*y = e
# c*x + d*y = f

#input numbers
a=float(input("enter a = "))
b=float(input("enter b = "))
c=float(input("enter c = "))
d=float(input("enter d = "))
e=float(input("enter e = "))
f=float(input("enter f = "))
# Coefficients
Coefficients = np.array([[a, b], [c, d]])

# Fixed values
Fixed_values = np.array([e, f])

print("Solution of linear equations:", np.linalg.solve(Coefficients , Fixed_values))
