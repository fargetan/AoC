# filename = 'test.txt'
# puzzleInput=[]
# filename = 'input.txt'
# puzzleInput=[]

# initialize input 
# with open(filename) as file:
#   for line in file:
#     puzzleInput.append(line)
    
#puzzleInput = [1,3,2]
#puzzleInput = [1,20,8,12,0,14]
puzzleInput = [14,0,12,8,20,1]
lastNumber = puzzleInput[0]
previousNumbers = puzzleInput[:]
count = len(puzzleInput)
while True:
  if lastNumber in previousNumbers[1:]:
    for i in range(1, len(previousNumbers)):
      if lastNumber == previousNumbers[i]:
        previousNumbers.insert(0, i)
        break
  else: 
    previousNumbers.insert(0, 0)
  count += 1
  lastNumber = previousNumbers[0]
  if count == 30000000:
    print( count, lastNumber )
    break
  #print( count, lastNumber )
  #print( previousNumbers )
  
