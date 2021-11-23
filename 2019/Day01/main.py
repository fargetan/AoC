from math import floor
data = []
filename = "input.txt"
with open(filename, 'r') as datafile:
  for line in datafile:
    data.append(int(line))

#print(data)

def getFuel(mass):
  fuel = 0
  total = 0
  while fuel >= 0:
    fuel = floor(mass/3) - 2
    if fuel >= 0:
      total += fuel
      mass = fuel
      # print(mass)
  return total

# calculate initial fuel
 
# use output to recalc
totalFuel = 0

# print(getFuel(12))
# print(getFuel(14))
# print(getFuel(1969))
# print(getFuel(100756))

for module in data:
  #print(getFuel(module))
  totalFuel += getFuel(module)

print(totalFuel)