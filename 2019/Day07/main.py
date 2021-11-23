 # Intcode Computer
def compute(_input_, inPos, program):
  position = 0
  output = []
  instruction = program[position]
  
  counter = 1

  while instruction != 99:
  # 
    instruction = program[ position ]
    opcode = instruction%100
    #print( str(instruction) + ", " + str(_input_))
    #print("run number" + str(counter))
    #print(instruction)
    #print(position)
    #print(opcode)
    
    params = str(instruction)[:-2]
    #print(params)
    modes = []
    for param in params:
      if param == '0': modes.append(False)
      else: modes.append(True)
      #print(modes)
    if len(modes) == 2:
      modes = [False, modes[0], modes[1]]
    if len(modes) == 1:
      modes = [False, False, modes[0]]
    if len(modes) == 0:
      modes = (False, False, False)
    #print(modes)

    #addition and multiplication
    if (opcode == 1) or (opcode == 2):
      if modes[2]: val1 = program[ position + 1 ]
      else: val1 = program[ program[ position + 1 ] ]
      if modes[1]: val2 = program[ position + 2 ]
      else: val2 = program[ program[ position + 2 ] ]
      if modes[0]: val3 = program [ position + 3]
      else: val3 = program [ position + 3 ]
      if opcode == 1:
        #print("adding")
        program[ val3 ] = val1 + val2
      else:
        #print('multiplying')
        program[ val3 ] = val1 * val2
      position += 4


    # input and output
    if opcode == 3 or opcode == 4:
      val1 = program[ position + 1 ]
      if opcode == 3:
        #print('taking input')
        program[val1] = _input_[inPos]
        inPos += 1
      if opcode == 4:
        #print('outputting')
        if modes[2]: output.append(val1)
        else: 
          val1 = program[val1]
          output.append(val1)
          #print(val1)
        return val1
      position += 2

    # jump if true
    if opcode == 5:
      # get next two values
      val1 = program[position + 1]
      val2 = program[position + 2]
      # get values if not immediate mode
      if not modes[2]: val1 = program[val1]
      if not modes[1]: val2 = program[val2]
      # check if first value is nonzero and update pointer
      if val1 != 0: position = val2
      else: position += 3
    
    #jump if false
    if opcode == 6:
      # get next two values
      val1 = program[position + 1]
      val2 = program[position + 2]
      # get values if not immediate mode
      if not modes[2]: val1 = program[val1]
      if not modes[1]: val2 = program[val2]
      # check if first value is nonzero and update pointer
      if val1 == 0: position = val2
      else: position += 3

    #less than
    if opcode == 7:
      # get next two values
      val1 = program[position + 1]
      val2 = program[position + 2]
      val3 = program[position + 3]
      # get values if not immediate mode
      if not modes[2]: val1 = program[val1]
      if not modes[1]: val2 = program[val2]
      # check if first value is nonzero and update pointer
      if val1 < val2 : program[val3] = 1
      else: program[val3] = 0
      position += 4

    #equals
    if opcode == 8:
      # get next two values
      val1 = program[position + 1]
      val2 = program[position + 2]
      val3 = program[position + 3]
      # get values if not immediate mode
      if not modes[2]: val1 = program[val1]
      if not modes[1]: val2 = program[val2]
      # check if first value is nonzero and update pointer
      if val1 == val2 : program[val3] = 1
      else: program[val3] = 0
      position += 4


    if opcode not in  [1, 2, 3, 4, 5, 6, 7, 8, 99]:
      print("error")
      print(position)
      print(opcode)
      instruction = 99
  # output is in slot 0
    counter += 1
    #print(output)
  return data[0]

#print(compute(1, data))
#print(data)
#data = [3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0]
data = [3,8,1001,8,10,8,105,1,0,0,21,30,51,72,81,94,175,256,337,418,99999,3,9,101,5,9,9,4,9,99,3,9,1001,9,3,9,1002,9,2,9,1001,9,2,9,1002,9,5,9,4,9,99,3,9,1002,9,4,9,101,4,9,9,102,5,9,9,101,3,9,9,4,9,99,3,9,1002,9,4,9,4,9,99,3,9,102,3,9,9,1001,9,4,9,4,9,99,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,99,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,99,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,99]

def runThrustSim(phases):
  _inputs_ = [0]
  inPos = 0
  #print(compute(_inputs_, inPos, data))

  nextInput = 0

  for i in phases:
    inPos = 0
    phase = i
    _inputs_ = [i, nextInput]
    nextInput = compute(_inputs_, inPos, data)

  return nextInput

possibles = [[4,3,2,1,0], [0,1,2,3,4]]

from itertools import permutations

possibles = list(permutations(range(5)))

maxThrust = 0
maxPhases = []
for j in possibles:
  thrust = runThrustSim(j)
  if thrust > maxThrust:
    maxThrust = thrust
    maxPhases = j

print(maxThrust)
print(maxPhases)

