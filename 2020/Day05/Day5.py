# get input
lines = []
with open('input.txt') as file:
  for line in file:
    lines.append(line)

def getRow( rowString, rows ):
  for rowHalf in rowString:
    rows = halveRow( rowHalf, rows )
    # print(rows)
  return rows[0]

def halveRow( half, rows ):
  if half == "F":
    return rows[:int(len(rows)/2)]
  else : return rows[int(len(rows)/2):]

def getCol( colString, cols ):
  for colHalf in colString:
    cols = halveCol( colHalf, cols )
    # print(cols)
  return cols[0]

def halveCol( half, cols ):
  if half == "L":
    return cols[:int(len(cols)/2)]
  else : return cols[int(len(cols)/2):]

def getSeatID( passString, rows, cols ):
  row = getRow( passString[:7], rows )
  col = getCol( passString[7:-1], cols )
  return 8 * row + col

rows = [ i for i in range(128)]
cols = [ i for i in range(8)]

# print(getRow( "FBFBBFF", rows ))
# print(getCol( "RLR", cols))

#print(getSeatID( "FBFBBFFRLR\n", rows, cols ))
seats=[]
for i in lines:
  seats.append(getSeatID( i, rows, cols ))

print(max(seats))
seats.sort()
for i in range(len(seats)):
  if seats[i] - seats[i+1] == -2:
    print(seats[i])
    print(seats[i+1])
    break
