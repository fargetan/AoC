data = []

#with open('test.txt', 'r') as file:
#with open('test2.txt', 'r') as file:
with open('input.txt', 'r') as file:
  for line in file:
    newRow = line.strip().split(')')
    data.append(newRow)

def buildMap(instructions):
  _Map_ = {}
  for row in instructions:
    if row[0] in _Map_:
      _Map_[row[0]].append(row[1])
    else:
      _Map_[row[0]] = [row[1]]
  return _Map_  

starMap = buildMap(data)
#print(starMap)

if 'COM' in starMap:
  print('found')

#recursion to get orbits
def FindNext(starname, mapp, orbits, depth, depthDict):
  # increase level
  depth += 1
  # get leaves
  stars = mapp[starname]
  # print(stars)
  # find next
  for star in stars:
    # if star has other orbitals, get those
    if star in mapp:
      FindNext(star, mapp, orbits, depth, depthDict)
    # if star does not have orbitals, send back the depth
    depthDict[star] = depth

depths = {}
orbits = 0
depth = 0
FindNext('COM', starMap, orbits, depth, depths)

print(depths)
total = 0
for item in depths:
  total += depths[item]

print(total)

# part 2
# Find the paths to each?
# search for name 
def FindStarPath(starName, path):
  for star in starMap:
    parent = star
    if starName in starMap[parent]:
      path.append(parent)
      FindStarPath(parent, path)

# stop at COM
pathToYou = []
pathToSan = []
FindStarPath('YOU', pathToYou)
# print(pathToYou)
FindStarPath('SAN', pathToSan)
# print(pathToSan)

commons = []
for i in pathToYou:
  for j in pathToSan:
    if i == j:
      commons.append(i)

for item in commons:
  pathToSan.remove(item)
  pathToYou.remove(item)
# print(pathToYou)
# print(pathToSan)
print( (len(pathToYou) + len(pathToSan)) )