# get input
bags = {}

def countAll( bagDict, color ):
  # get number of bags open
  contents = bagDict[color]
  numOfBags = 1 # <-- self
  #print("looking in ", color, " current count: ", totalCount)
  
  if len(contents) == 0 : return 1
  
  for i in contents:
    # add number of inner bags * their count of bags inside
    numOfBags += bagDict[color][i] * countAll( bagDict, i )
  #print("finished in ", color, " current count: ", numOfBags)
  return numOfBags

with open('input.txt') as file:
  for line in file:
    halves = line.split(" bags contain ")
    bagName = halves[0].strip()
    contentsList = halves[1].split(',')
    if contentsList[0].strip() == 'no other bags.':
      bags[bagName] = {}
    else: 
      contents = {}
      for entry in contentsList:
        innerBag = ' '.join(entry.split()[1:3])
        number = int(entry.split()[0])
        contents[innerBag] = number
      bags[bagName] = contents

count = 0
# for bag in bags.keys():
  # print(bag, bags[bag])
print(countAll(bags, 'shiny gold'))


""" First Half of the Challenge Below 

with open('input.txt') as file:
  for line in file:
    halves = line.split(" bags contain ")
    bagName = halves[0].strip()
    contentsList = halves[1].split(',')
    if contentsList[0].strip() == 'no other bags.':
      contents = []
    else: 
      contents = []
      for entry in contentsList:
        innerBag = ' '.join(entry.split()[1:3])
        contents.append(innerBag)
    bags[bagName] = contents

# for bag in bags.keys():
  # print(bags[bag])

def countBags( bags, color, bagsWith ):
  for bag in bags.keys():
    if color in bags[bag]:
      # print("found ", color, " in", bag)
      bagsWith.append(bag)
      countBags( bags, bag, bagsWith )
  return bagsWith

def countBagsInGold( bags, color, totalCount )


bagsWithGold = []

bagsWithGold = countBags( bags, "shiny gold", bagsWithGold )

print(len(set(bagsWithGold)))

"""
