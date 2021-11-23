# filename = 'test.txt'
filename = 'input.txt'

puzzleInput = []
with open(filename) as file:
  for line in file:
    puzzleInput.append(line)
    
    
testing = puzzleInput[:10]
# split on spaces

def getValue( expression ):
  for char in list(expression):
    if char == ' ':
      continue
print(test)

