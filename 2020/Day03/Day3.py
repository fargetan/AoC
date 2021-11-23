# get input
treeMap = []
with open('input.txt') as file:
  for line in file:
    row = []
    # turn line into a list
    for i in line[:-1]:
      row.append(i) 
    # append the row
    treeMap.append(row)

# test = treeMap[:10]

# print(test)

def countTrees( treeMapp ):
  xpos = 0
  ypos = 0
  width = len(treeMapp[0])
  treeCount = 0
  while ypos < len(treeMapp) - 1:
    # move positions
    xpos += 3
    ypos += 1

    # must wrap around since trees continue 
    if xpos >= width:
      xpos -= width

    # print(xpos)
    # print(ypos)

    print( treeMapp[ypos][xpos])
    # check for tree 
    if treeMapp[ypos][xpos] == '#':
      treeCount += 1
      print("ouch")

  return treeCount

def countTrees_2( treeMapp , rise, run ):
  xpos = 0
  ypos = 0
  width = len(treeMapp[0])
  treeCount = 0
  while ypos < len(treeMapp) - 1:
    # move positions
    xpos += run 
    ypos += rise 

    # must wrap around since trees continue 
    if xpos >= width:
      xpos -= width

    # print(xpos)
    # print(ypos)

    # print( treeMapp[ypos][xpos])
    # check for tree 
    if treeMapp[ypos][xpos] == '#':
      treeCount += 1
      # print("ouch")

  return treeCount

# print(countTrees(treeMap))

rises = [ 1, 1, 1, 1, 2 ]
runs = [ 1, 3, 5, 7, 1 ]
counts = []
for i in range(5):
  count = countTrees_2( treeMap, rises[i], runs[i])
  print( count )
  counts.append( count)

total = 1
for j in counts:
  total = total * j

print(total)