from math import tan, pi

l = float(input('Enter the length of the sides:'))
n = int(input('Enter the number of sides:'))

# area = (n * l squared) / (4 * tan(PI / n))

area = (n * l**2) / (4 * tan(pi/n))

print('The area of the polygon is %.2f' % area)