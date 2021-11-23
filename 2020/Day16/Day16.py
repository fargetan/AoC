# filename = 'test.txt'
filename = 'input.txt'

puzzleInput = []
with open(filename) as file:
  for line in file:
    puzzleInput.append(line)
    
fields = []
for row in puzzleInput[:20]:
  fields.append(row.split(':')[1].strip())
myTicket = puzzleInput[22].strip().split(',')
nearbyTickets = []
for row in puzzleInput[25:]:
  row = row.strip()
  nearbyTickets.append(row.split(','))

print(fields)
print(myTicket)
print(nearbyTickets[0])

# combine valid ranges
# by visually checking valid is 
# 26-973
total = 0

for ticket in nearbyTickets:
  for entry in ticket:
    num = int(entry)
    if num < 26 or num > 973:
      total+=num
# check each nearby ticket for invalid numbers 
# sum the invalid numbers 

print(total)

# exclude invalid tickets 
# find fields that are valid across 
# all tickets
# try first ticket and reorder fields
# until they match
# repeat for all tickets
# if cycle through all tickets
# with no changes, finalize reorder
