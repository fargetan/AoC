# filename = 'test.txt'
# preLength = 5
filename = 'input.txt'
preLength = 25


numArr = []

with open(filename) as file:
  for line in file:
    numArr.append(int(line.strip()))

def checkValid( num, addendArr ):
  for i in range(len(addendArr)):
    for j in range(len(addendArr)):
      if i != j:
        if addendArr[i] + addendArr[j] == num:
          return True

  return False

# find firs invalid number
while True:
  for k in range(preLength, len(numArr)):
    addends = numArr[k - preLength : k]
    #print(numArr[k], addends)
    if not checkValid( numArr[k], addends ):
      invalidNum = numArr[k]
      break
  break

print(invalidNum)
# search for string of numbers than add to invalid
# number
# initialize a couple "pointers"
first = 0
last = 0

while True:
  # get slice
  numSlice = numArr[ first : last ]
  # check sum of slice for answer
  if sum(numSlice) == invalidNum:
    # sort slice
    numSlice.sort()
    print(numSlice[0] + numSlice[-1])
    break
  # check if sum > invalid number
  # and reinitialize first and last
  elif sum(numSlice) > invalidNum:
    first += 1
    last = first + 0
  # if neither of the above are True
  # increment last pointer and go back to top 
  else: 
    last += 1
  