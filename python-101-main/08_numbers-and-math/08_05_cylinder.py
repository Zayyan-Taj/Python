# Write the necessary code calculate the volume and surface area
# of a cylinder with a radius of 3.14 and a height of 5.
# Print out the result.


import math

radius = 3.14
height = 5

volume = math.pi * radius**2 * height
surface_area = 2 * math.pi * radius * height + 2 * math.pi * radius**2

print("The volume of the cylinder is", volume)
print("The surface area of the cylinder is", surface_area)