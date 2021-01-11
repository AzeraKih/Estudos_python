##Consider a sphere with radius 2.5. Determine its surface area and volume,
##and display them in separate lines.
##
##Make use of 'pi' defined in the 'math' module.
##
##Hint: (Surface area = 4pir^2 ; Volume = 4/3pir^3).

from math import pi

radius = 2.5

suface= 4*pi*(radius**2)

volume = 4/3*pi*(radius**3)

print(suface)
print(volume)
