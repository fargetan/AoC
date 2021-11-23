#data = []
#filename = "input.txt"
#with open(filename, 'r') as datafile:
#  for line in datafile:
#    data.append(int(line))

#data = [1,9,10,3,2,3,11,0,99,30,40,50]
#data = [1,1,1,4,99,5,6,0,99]
initData = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,13,19,1,9,19,23,2,13,23,27,2,27,13,31,2,31,10,35,1,6,35,39,1,5,39,43,1,10,43,47,1,5,47,51,1,13,51,55,2,55,9,59,1,6,59,63,1,13,63,67,1,6,67,71,1,71,10,75,2,13,75,79,1,5,79,83,2,83,6,87,1,6,87,91,1,91,13,95,1,95,13,99,2,99,13,103,1,103,5,107,2,107,10,111,1,5,111,115,1,2,115,119,1,119,6,0,99,2,0,14,0]

# For Part 2
for noun in range(100):
  for verb in range(100):
    data = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,13,19,1,9,19,23,2,13,23,27,2,27,13,31,2,31,10,35,1,6,35,39,1,5,39,43,1,10,43,47,1,5,47,51,1,13,51,55,2,55,9,59,1,6,59,63,1,13,63,67,1,6,67,71,1,71,10,75,2,13,75,79,1,5,79,83,2,83,6,87,1,6,87,91,1,91,13,95,1,95,13,99,2,99,13,103,1,103,5,107,2,107,10,111,1,5,111,115,1,2,115,119,1,119,6,0,99,2,0,14,0]
    data[1] = noun
    data[2] = verb

    # Intcode Computer
    instruction = 0 
    position = 0
    while instruction != 99:
    # read next 4
      instruction = data[ position ]
      if instruction != 99:
        val1 = data[ data[ position + 1 ] ]
        val2 = data[ data[ position + 2 ] ]
        storeLoc = data [ position + 3 ]

      if instruction == 1:
        data[ storeLoc ] = val1 + val2
      else:
        if instruction == 2:
          data[ storeLoc ] = val1 * val2
        else:
          if instruction != 99:
            #print("error")
            instruction = 99
      position += 4

    if data[0] == 19690720: 
      print(str(noun) + " " + str(verb)+ " " + str(data[0]))

    #print(str(noun) + " " + str(verb) + " " + str(data[0]))
    #print(str(data[0]) + " " + str(data[1]) + " " + str(data[2]))


