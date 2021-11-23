# get input
lines = []
with open('input.txt') as file:
  for line in file:
    lines.append(line.strip())

def getAnswers( listOfAnswers ):
  questions = 'abcdefghijklmnopqrstuvwxyz'
  characterDict = {}
  count = 0
  for a in questions:
    characterDict[a] = 0

  # iterate through all lines
  for line in listOfAnswers:
    # if line is not blank:
    if line != "":
      # for every char in the line
      for character in line:
        # set each question to 1 
        characterDict[character] = 1
    # if the line is blank, add count and clear dictionary
    if line == "":
      count += sum([characterDict[x] for x in characterDict.keys()])
      for j in characterDict.keys():
        characterDict[j] = 0
  return count

def getAnswers2( listOfAnswers ):
  questions = 'abcdefghijklmnopqrstuvwxyz'
  characterDict = {}
  count = 0
  groupSize = 0
  questCount = 0
  for a in questions:
    characterDict[a] = 0

  # iterate through all lines
  for line in listOfAnswers:
    # if line is not blank:
    if line != "":
      # count the people in the group
      groupSize += 1
      # for every char in the line
      for character in line:
        # add one to each question in the dict 
        characterDict[character] += 1
    # if the line is blank, add count and clear dictionary
    if line == "":
      for char in characterDict.keys():
        if characterDict[char] == groupSize:
          questCount += 1
      count += questCount
      for j in characterDict.keys():
        characterDict[j] = 0
      questCount = 0
      groupSize = 0
  return count


# iterate through lines and get count of yes answers per group

answers = getAnswers( lines )
#print(lines)
print(answers)

print(getAnswers2( lines ))