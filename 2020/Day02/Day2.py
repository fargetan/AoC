# get input
pwords = []
with open('input.txt') as file:
  for line in file:
    # append the text line as an integer
    pwords.append(line.strip())

test = pwords[:10]

# print(test)

# function to take a policy and password combo
# and return whether the password is valid as a 
# boolean

def checkAgain( policyAndPass ):
  # split string on colon 
  # to get password and policy
  halves = policyAndPass.split(':')
  password = halves[1].strip()
  # get char to search for
  searchChar = halves[0].split()[1].strip()
  positions = halves[0].split()[0].strip().split('-')
  # no index zero in the policy
  pos1 = int(positions[0]) - 1
  pos2 = int(positions[1]) - 1

  # print( password )
  # print( searchChar )
  # print( pos1 )
  # print( pos2 )

  # start count 
  count = 0

  # check both positions
  if password[ pos1 ] == searchChar: count += 1
  if password[ pos2 ] == searchChar: count += 1


  # count must be exactly 1
  if count == 1:
    return True
  
  else: return False

# print( test[0] )
# print(checkPass(test[0]))

def checkPass( policyAndPass ):
    # assume invalid
  valid = False

  # split string on colon 
  # to get password and policy
  halves = policyAndPass.split(':')
  password = halves[1].strip()
  # get char to search for
  searchChar = halves[0].split()[1].strip()
  minMax = halves[0].split()[0].strip().split('-')
  minimum = int(minMax[0])
  maximum = int(minMax[1])

  # print( searchChar )
  # print( minimum )
  # print( maximum )

  # start count 
  count = 0

  for a in password:
    if a == searchChar:
      count += 1

  if count in range( minimum, maximum + 1 ):
    valid = True
  # print( password )
  # print( count )
  # print( valid )
  return valid
# print( test[0] )
# print(checkPass(test[0]))

total = 0
for item in pwords:
  if checkAgain( item ): 
    # print( 'True' )
    total += 1

print(total)