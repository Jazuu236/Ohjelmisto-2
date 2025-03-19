import numpy as np
#Tehtävä 1.1.
a1 = 2.493
b1 = 0.911

print("Tehtävän 1.1. a:n ja b:n vastaus:")
print(np.degrees(a1))
print(np.degrees(b1))

#Tehtävä 1.2.
a2 = 137.7
b2 = 62.3

print("Tehtävän 1.2. a:n ja b:n vastaus:")
print(np.radians(a2))
print(np.radians(b2))

#Tehtävä 1.3.
asteet = np.array([30, 45, 60, 90, 120, 135, 150, 180, 270, 360])

radiaanit = np.radians(asteet)
taulukko = np.column_stack((asteet, radiaanit))

print(taulukko)