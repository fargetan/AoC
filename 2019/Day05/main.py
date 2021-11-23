#data = []
#filename = "input.txt"
#with open(filename, 'r') as datafile:
#  for line in datafile:
#    data.append(int(line))

#data = [1,9,10,3,2,3,11,0,99,30,40,50]
#data = [1,1,1,4,99,5,6,0,99]
#Day2 data
#data = [1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,13,19,1,9,19,23,2,13,23,27,2,27,13,31,2,31,10,35,1,6,35,39,1,5,39,43,1,10,43,47,1,5,47,51,1,13,51,55,2,55,9,59,1,6,59,63,1,13,63,67,1,6,67,71,1,71,10,75,2,13,75,79,1,5,79,83,2,83,6,87,1,6,87,91,1,91,13,95,1,95,13,99,2,99,13,103,1,103,5,107,2,107,10,111,1,5,111,115,1,2,115,119,1,119,6,0,99,2,0,14,0]

#data = [1002,4,3,4,33]
#data =[3,0,4,0,99]
#Day 5 data
data = [3,225,1,225,6,6,1100,1,238,225,104,0,1102,46,47,225,2,122,130,224,101,-1998,224,224,4,224,1002,223,8,223,1001,224,6,224,1,224,223,223,1102,61,51,225,102,32,92,224,101,-800,224,224,4,224,1002,223,8,223,1001,224,1,224,1,223,224,223,1101,61,64,225,1001,118,25,224,101,-106,224,224,4,224,1002,223,8,223,101,1,224,224,1,224,223,223,1102,33,25,225,1102,73,67,224,101,-4891,224,224,4,224,1002,223,8,223,1001,224,4,224,1,224,223,223,1101,14,81,225,1102,17,74,225,1102,52,67,225,1101,94,27,225,101,71,39,224,101,-132,224,224,4,224,1002,223,8,223,101,5,224,224,1,224,223,223,1002,14,38,224,101,-1786,224,224,4,224,102,8,223,223,1001,224,2,224,1,223,224,223,1,65,126,224,1001,224,-128,224,4,224,1002,223,8,223,101,6,224,224,1,224,223,223,1101,81,40,224,1001,224,-121,224,4,224,102,8,223,223,101,4,224,224,1,223,224,223,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,1008,677,226,224,1002,223,2,223,1005,224,329,1001,223,1,223,107,677,677,224,102,2,223,223,1005,224,344,101,1,223,223,1107,677,677,224,102,2,223,223,1005,224,359,1001,223,1,223,1108,226,226,224,1002,223,2,223,1006,224,374,101,1,223,223,107,226,226,224,1002,223,2,223,1005,224,389,1001,223,1,223,108,226,226,224,1002,223,2,223,1005,224,404,1001,223,1,223,1008,677,677,224,1002,223,2,223,1006,224,419,1001,223,1,223,1107,677,226,224,102,2,223,223,1005,224,434,1001,223,1,223,108,226,677,224,102,2,223,223,1006,224,449,1001,223,1,223,8,677,226,224,102,2,223,223,1006,224,464,1001,223,1,223,1007,677,226,224,1002,223,2,223,1006,224,479,1001,223,1,223,1007,677,677,224,1002,223,2,223,1005,224,494,1001,223,1,223,1107,226,677,224,1002,223,2,223,1006,224,509,101,1,223,223,1108,226,677,224,102,2,223,223,1005,224,524,1001,223,1,223,7,226,226,224,102,2,223,223,1005,224,539,1001,223,1,223,8,677,677,224,1002,223,2,223,1005,224,554,101,1,223,223,107,677,226,224,102,2,223,223,1006,224,569,1001,223,1,223,7,226,677,224,1002,223,2,223,1005,224,584,1001,223,1,223,1008,226,226,224,1002,223,2,223,1006,224,599,101,1,223,223,1108,677,226,224,102,2,223,223,1006,224,614,101,1,223,223,7,677,226,224,102,2,223,223,1005,224,629,1001,223,1,223,8,226,677,224,1002,223,2,223,1006,224,644,101,1,223,223,1007,226,226,224,102,2,223,223,1005,224,659,101,1,223,223,108,677,677,224,1002,223,2,223,1006,224,674,1001,223,1,223,4,223,99,226]

  # Intcode Computer
def compute(_input_, program):
  position = 0
  output = []
  instruction = program[position]
  
  counter = 1

  while instruction != 99:
  # 
    instruction = program[ position ]
    opcode = instruction%100
    print( str(instruction) + ", " + str(_input_))
    print("run number" + str(counter))
    print(instruction)
    print(position)
    print(opcode)
    
    params = str(instruction)[:-2]
    print(params)
    modes = []
    for param in params:
      if param == '0': modes.append(False)
      else: modes.append(True)
      print(modes)
    if len(modes) == 2:
      modes = [False, modes[0], modes[1]]
    if len(modes) == 1:
      modes = [False, False, modes[0]]
    if len(modes) == 0:
      modes = (False, False, False)
    print(modes)

    #addition and multiplication
    if (opcode == 1) or (opcode == 2):
      if modes[2]: val1 = program[ position + 1 ]
      else: val1 = program[ program[ position + 1 ] ]
      if modes[1]: val2 = program[ position + 2 ]
      else: val2 = program[ program[ position + 2 ] ]
      if modes[0]: val3 = program [ position + 3]
      else: val3 = program [ position + 3 ]
      if opcode == 1:
        print("adding")
        program[ val3 ] = val1 + val2
      else:
        print('multiplying')
        program[ val3 ] = val1 * val2
      position += 4


    # input and output
    if opcode == 3 or opcode == 4:
      val1 = program[ position + 1 ]
      if opcode == 3:
        print('taking input')
        program[val1] = _input_
      if opcode == 4:
        print('outputting')
        if modes[2]: output.append(val1)
        else: output.append(program[val1])
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
    print(output)
  return data[0]

#print(compute(1, data))
#print(data)
print(compute(5, data))