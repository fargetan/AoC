# get input
lines = []
with open('input.txt') as file:
  for line in file:
    lines.append(line)


def checkValid( fieldStates ):
  # enumerate fields to check 
  fieldsToCheck = [ 'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', ]
  # for each of these, if it is False return False
  for j in fieldsToCheck:
    if fieldStates[j] == False: return False
  # if still here, they must all be True
  return True

def checkByr( year ):
  valid = False
  byr = int(year)
  if byr in range(1920, 2003): valid = True
  return valid

def checkIyr( year ):
  valid = False
  iyr = int(year)
  if iyr in range(2010, 2021): valid = True
  return valid

def checkEyr( year ):
  valid = False
  eyr = int(year)
  if eyr in range(2020, 2031): valid = True
  return valid

def checkHgt( height ):
  valid = False
  hgtArray = [x for x in height ]
  # print(hgtArray)
  
  units = ''.join(hgtArray[-2:])
  
  if units == 'cm':
    measurement = int(''.join(hgtArray[:-2]))
    if measurement in range(150, 194): valid = True
  elif units == 'in':
    measurement = int(''.join(hgtArray[:-2]))
    if measurement in range(59, 77): valid = True
  
  return valid

def checkHcl( hair ):
  valid = True
  validChars = '0123456789abcdefABCDEF'
  hairArray = [x for x in hair ]
  
  if hairArray[0] == '#' and len(hairArray) == 7:
    for i in hair[1:]:
      if i not in validChars: valid = False
  else: valid = False
  return valid

def checkEcl( eye ):
  validEyes = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
  valid = False 
  if eye in validEyes: valid = True

  return valid 

def checkPid( pid ):
  valid = True
  validChars = '0123456789'
  #pidArray = [x for x in pid ]
  # print(pid)
  if len(pid) == 9:
    for i in pid:
      if i not in validChars: valid = False
  else: valid = False
  return valid



def checkValid2( fieldDict ):
  fields = [ 'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid' ]
  fieldStates = {}
  for i in fields:
    fieldStates[ i ] = False
  
  for field in fieldDict:
    if field == fields[0]:
      fieldStates[field]= checkByr( fieldDict[field] )
    if field == fields[1]:
      fieldStates[field] = checkIyr( fieldDict[field] )
    if field == fields[2]:
      fieldStates[field] = checkEyr( fieldDict[field] )
    if field == fields[3]:
      fieldStates[field] = checkHgt( fieldDict[field] )
    if field == fields[4]:
      fieldStates[field] = checkHcl( fieldDict[field] )
    if field == fields[5]:
      fieldStates[field] = checkEcl( fieldDict[field] )
    if field == fields[6]:
      fieldStates[field] = checkPid( fieldDict[field] )
    
  for item in fieldStates:
    if fieldStates[item] == False: return False
  return True


def checkPass( dba ):
  fields = [ 'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']

  fieldStates = {}
  totalValid = 0
  for i in fields:
    fieldStates[ i ] = False
  
  # iterate through all lines
  
  for line in dba:
  
    # look for new line and reset fieldStates
    if line == '\n':
      # print('found newline')
      for i in fieldStates:
        fieldStates[i] = False

    # separate line to passport key/value pairs 
    passFields = line.split()
    moreThanCid = True
    # get the fieldnames and set each State to True  
    for item in passFields:
      fieldName = item.split(':')[0]
      if fieldName in fields:
        fieldStates[fieldName] = True

    # now check to see if all required fields 
    # are present and increment counter
    presentValid = checkValid( fieldStates )

    if presentValid:
      totalValid += 1
    
    # undo that if this is only a line with the optional
    # field of 'cid'
    if presentValid and len(passFields) == 1 and line.split(':')[0] == 'cid':
      totalValid -= 1


  return totalValid

def checkPass2( dba ):
  fields = [ 'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']

  fieldStates = {}
  passport = {}
  totalValid = 0
  for i in fields:
    fieldStates[ i ] = False
  
  # iterate through all lines
  
  for line in dba:
  
    # look for new line and reset fieldStates
    if line == '\n':
      # print('found newline')
      for i in fieldStates:
        fieldStates[i] = False

    moreThanCid = True
    # separate line to passport key/value pairs 
    passFields = line.split()

    # get the fieldnames and set each State to True  
    for item in passFields:
      fieldName = item.split(':')[0]
      fieldValue = item.split(':')[1]
      if fieldName in fields:
        fieldStates[fieldName] = True
        passport[fieldName] = fieldValue
    
    # ignore next if this is only a line with the optional
    # field of 'cid'
    if len(passFields) == 1 and line.split(':')[0] == 'cid':
      moreThanCid = False
    # now check to see if all required fields 
    # are present and increment counter
    hasFields = checkValid( fieldStates )

    if hasFields and moreThanCid and checkValid2( passport ):
      totalValid += 1


  return totalValid


print(checkPass2( lines ))
