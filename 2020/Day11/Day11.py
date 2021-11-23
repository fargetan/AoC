# filename = 'test.txt'
# puzzleInput=[]
filename = 'input.txt'
puzzleInput=[]

# initialize input 
with open(filename) as file:
  for line in file:
    puzzleInput.append(list(line.strip()))

rows = len(puzzleInput)
seats = len(puzzleInput[0])

def applyRule( lobbyLayout ):
  newLobby = []
  for row in range(rows):
    newSeats = []
    for seat in range(seats):
      newSeats.append( str(checkSeat( row, seat, lobbyLayout) ) )
    newLobby.append(newSeats)
  return newLobby

def applyRule2( lobbyLayout ):
  newLobby = []
  for row in range(rows):
    newSeats = []
    for seat in range(seats):
      newSeats.append( str(checkSeat2( row, seat, lobbyLayout) ) )
    newLobby.append(newSeats)
  return newLobby

def lookDir( leftRight, upDown, mapp, rowNum, seatNum ):
  firstRow = rowNum + upDown
  firstSeat = seatNum + leftRight
  
  while firstRow in range(rows) and firstSeat in range(seats):
    adjacentSquare = mapp[firstRow][firstSeat]
    
    if adjacentSquare == "#":
      return 1
    elif adjacentSquare == "L":
      return 0
    firstRow += upDown
    firstSeat += leftRight
  return 0

def checkSeat2( r, s, mapp ):
  refMap = mapp[:]
  occupied = 0
  currentState = refMap[r][s]
  for dir1 in [ -1, 0 , 1]:
    for dir2 in [ -1, 0 , 1]:
      if not (dir1 == dir2 == 0) :
        occupied += lookDir( dir1, dir2, refMap, r, s)
  
  if currentState == "#" and occupied > 4:
    return "L"
  elif currentState == "L" and occupied == 0:
    return "#"
  else: return refMap[r][s]

def checkSeat( r, s, mapp ):
  
  refMap = mapp[:]
  occupied = 0
  for x in range(r-1, r+2):
    if x in range(rows):
      for y in range(s-1,s+2):
        if y in range(seats):
          if not (x == r and y == s):
            #print('checking ', x, ' and ', y)
            if mapp[x][y] == "#":
              #print('found a person')
              occupied += 1
  if refMap[r][s] == "#" and occupied > 3:
    return "L"
  elif refMap[r][s] == "L" and occupied == 0:
    return "#"
  else: return refMap[r][s]


""" testing code
for i in range(rows):
  print(puzzleInput[i])
print('')
initLobby= puzzleInput[:]
updated = applyRule(initLobby[:])
for i in range(rows):
  print(updated[i])
print('')
updated = applyRule(updated)
for i in range(rows):
  print(updated[i])


for i in range(rows):
  print(puzzleInput[i])
print('')
initLobby= puzzleInput[:]
updated = applyRule2(initLobby[:])
for i in range(rows):
  print(updated[i])
print('')
updated = applyRule2(updated)
for i in range(rows):
  print(updated[i])

"""
# main Loop 

oldSeats = puzzleInput[:]
while True:

  # apply seating rule
  # new seats = rule(oldseats)
  newSeats = applyRule2(oldSeats[:])

  # check for change in seats 
  # if new_seats == old_seats
  if newSeats == oldSeats:
    break
  # break Loop 
  
  oldSeats = newSeats


# print number of occupied seats
count = 0

for row in oldSeats:
  for seat in row:
    if seat == "#":
      count += 1

print(count)