# Calculator to calculate the period of a mathematical pendulum with a certain starting angle
# Credit: Rafli Rizaldi/16021150 a.k.a QueenLy/LyFromQixing

import math

l = float(input("Insert the length of the rope in cm: "))
g = float(input("Insert the acceleration due to gravity g in m/s^2: "))
a = float(input("Enter the angle in degrees: "))

l_0 = l/100 # Convert the length of the rope to meters
rad = ((a)/180) * math.pi # Convert angle units to radians 
T_0 = (2*math.pi)*((l_0/g)**(1/2)) # Calculate the value of T before the expansion
expansion = (1+((1/4)*(math.sin(rad/2)**2)))+(((9/64)*(math.sin(rad/2)**4))) # Calculate the expansion value
T = T_0 * expansion # The value of the pendulum period with an initial angle can be determined by multiplying the initial T value by the expansion value

print("Theoretical period of a pendulum with an initial angle of " + str(a) + " degree" + " is " + str(round(T, 3)) + " s.")
