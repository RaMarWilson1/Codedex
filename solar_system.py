from math import pi 
from random import choice as ch 

planets = [
  'Mercury',
  'Venus',
  'Earth',
  'Mars',
  'Saturn'
]

random_planet = ch(planets)


if random_planet == 'Mercury':
    area = (4*pi*2440**2)
    print(round(area,3))
elif random_planet == 'Venus':
    area = (4*pi*6052**2)
    print(round(area,3))
elif random_planet == 'Earth':
    area = (4*pi*6371**2)
    print(round(area,3))
elif random_planet == 'Mars':
    area = (4*pi*3390**2)
    print(round(area,3))
elif random_planet == 'Saturn':
    area = (4*pi*58232**2)
    print(round(area,3))
else:
    print("Oops! An error occurred.")    
            