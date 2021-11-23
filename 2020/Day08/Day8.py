# filename = 'test.txt'
filename = 'input.txt'

instructions = []

with open(filename) as file:
  for line in file:
    instructions.append(line.strip())

accumulator = 0
positions = []
ip = 0 

def runProgram( instructions ):
  accumulator = 0
  positions = []
  ip = 0 
  while True:
    if ip in positions:
      return False

    positions.append(ip)
    instruction = instructions[ip].split()
    command = instruction[0]
    num = int(instruction[1].strip())

    # print("pointer ", ip) 
    # print('accumulator', accumulator)

    if command == 'acc':
      accumulator += num
      ip += 1 
    elif command == 'nop':
      ip += 1
    elif command == 'jmp':
      ip += num

    if ip >= len(instructions):
      print("accumulator: ", accumulator)
      return True

def rewrite( instructions, position ):
  # avoid pass-by-reference problem by 
  # copying list into new list
  program = instructions[:]
  initInstruction = program[ position ].split()
  if initInstruction[0] == 'nop':
    initInstruction[0] = 'jmp'
  if initInstruction[0] == 'jmp':
    initInstruction[0] = 'nop'
  program[ position ] = ' '.join(initInstruction) + '\n'
  return program

complete = False
posToChange = 0

while not complete:
  newProgram = rewrite( instructions, posToChange )
  complete = runProgram( newProgram )
  posToChange += 1

""" First Part Complete:
while True:
  if ip in positions:
    print(accumulator)
    break
  positions.append(ip)
  instruction = instructions[ip].split()
  command = instruction[0]
  num = int(instruction[1].strip())

  if command == 'acc':
    accumulator += num
    ip += 1 
  elif command == 'nop':
    ip += 1
  elif command == 'jmp':
    ip += num

"""