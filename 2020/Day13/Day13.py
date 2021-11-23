# filename = 'test.txt'
## puzzleInput=[]
filename = 'input.txt'
puzzleInput=[]

# initialize input 
with open(filename) as file:
  for line in file:
    puzzleInput.append(line)
    
buses = []
arrivalList = puzzleInput[1].split(',')

# only necessary for part 1
# start = int(puzzleInput[0].strip())
for num in puzzleInput[1].strip().split(','):
  buses.append(num)
  
  buses= [ int(x) for x in buses if x != 'x']

def checkSpot( mult, arrivalList ):
  # hop to multiple of first entry
  start = mult * int(arrivalList[0])
  for i in range(len(arrivalList)):
  # increment minute and check if multiple 
  # of bus at that index
    if arrivalList[i] == 'x':
      continue
    elif ( start + i ) % int(arrivalList[i]) != 0:
      return False
  return True
  
  # unless the element is 'x'
mult = 0
while True:
  if checkSpot( mult, arrivalList):
    print( mult * int(arrivalList[0]))
    break
  else: 
    mult += 1
  # if not mulitiple of bus, back to
  # step 1
    
"""    
# print(start, "\n", buses)

nextTime = start + 1000
nextBus = 0
# next bus 
for bus in buses:
  remainder = start % bus
  print( bus, remainder )
  busTime = start + bus - remainder
  print( busTime )
  if busTime < nextTime :
    nextBus = bus
    nextTime = busTime
    
print( nextBus * (nextTime - start ))
"""