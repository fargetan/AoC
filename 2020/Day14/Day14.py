# filename = 'test.txt'
# puzzleInput=[]
filename = 'input.txt'
puzzleInput=[]

# initialize input 
with open(filename) as file:
  for line in file:
    puzzleInput.append(line)
    

def updateMask( maskString ):
   list(maskString.strip())

def genAddresses( binaryList, addList ):
  # print("generating addresses")
  # print(binaryList)
  # print(addList)
  addresses1 = []
  addresses2 = []
  # upon end condition, add current address to list of addresses and return
  if 'X' not in binaryList:
    # print("no more Xs")
    addList.append(binaryList)
    return addList[:]
  else:
    for j in range(len(binaryList)):
      # print("at position ", j)
      if binaryList[j] == 'X':
        # print("found X at ", j)
        binaryList[j] = '0'
        # send new list with one less 'X' to gen addresses
        addresses1 = genAddresses(binaryList[:], addList)[:]
        # print('finished with 0 branch at ', j)
        # print(addresses1)
        binaryList[j] = '1'
        addresses2 = genAddresses(binaryList[:], addList)[:]
        # print('finished with 1 branch at ', j)
        # print(addresses2)
        # print(len(addresses1))
        # print(len(addresses2))
        for addr in addresses1:
          # print(addr)
          # print('adding addresses from 0 branch')
          addList.append(addr)
          # print('done adding from zero branch')
        for addr in addresses2:
          # print('adding addresses from 1 branch')
          addList.append(addr)
        return addList

def getAddresses( initAddress, mask ):
  # print( 'getting addresses')
  addresses = []
  # create list with the binary memory value
  binList = list(bin(initAddress)[2:])
  # pad left with zeros
  while len(binList) < len(mask):
    binList.insert(0, "0")
  # overwrite with any 1s or Xs from the mask
  # print("overwriting with 1s and Xs")
  # print(binList)
  for bitNum in range(len(mask)):
    if mask[bitNum] == '1' or mask[bitNum] == 'X':
      binList[bitNum] = mask[bitNum]
  # print(binList)
  # generate addresses by generating two for each X starting from left
  addresses = genAddresses(binList, addresses)
  return addresses


blankMask = [ 'x' for i in range(30)]
memory = {}

currMask = blankMask[:]

for line in puzzleInput:
  instruction = line.split(' = ')
  if instruction[0].strip() == 'mask':
    # print(instruction[1])
    currMask =  list( instruction[1].strip() )
    # print(len(currMask))
  elif instruction[0].strip()[:3] == 'mem':
    addBase = int(instruction[0].split('[')[1].split(']')[0])
    addrs = getAddresses( addBase, currMask)
    # print(addrs)
    for memLoc in addrs:
      memLoc = int(''.join(memLoc), 2)
      memory[memLoc] = int(instruction[1].strip())

total = 0
for a in memory:
  total += memory[a]

print(total)

""" Part One below
def writeMem( value, mask, mem ):
  # create list with the binary value
  binList = list(bin(value)[2:])
  # pad left with zeros
  while len(binList) < len(mask):
    binList.insert(0, "0")
  # overwrite value with mask value 
  for i in range(len(mask)):
    if mask[i] != 'X':
      binList[i] = str(mask[i])
  # change list back to binary and then 
  binString = '0b' + str(''.join(binList))
  newVal = int(binString, 2)
  return newVal

    

blankMask = [ 'x' for i in range(32)]
memory = {}

currMask = blankMask[:]

for line in puzzleInput:
  instruction = line.split(' = ')
  if instruction[0].strip() == 'mask':
    currMask =  list( instruction[1].strip() )
  elif instruction[0].strip()[:3] == 'mem':
    memLoc = instruction[0].split('[')[1].split(']')[0]
    memory[memLoc] = writeMem( int(instruction[1].strip()), currMask, memory )

# print(blankMask)
print(memory)
total = 0
for a in memory:
  total += memory[a]

print(total)
"""