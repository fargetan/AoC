# blank results list
candidates = []
"""
#generate list Part 1
for number in range(165432, 707913):
  adjacent = False
  increasing = True
  num = str(number)
  for i in range(5):
    if num[i] == num[i+1]:
      adjacent = True
    if num[i] > num[i+1]:
      increasing = False
  if (adjacent and increasing):
    candidates.append(i)

print(len(candidates))
"""
#generate list Part 2
for number in range(165432, 707913):
  adjacent = False
  increasing = True
  num = str(number)
  for i in range(5):
    if num[i] == num[i+1]:
      adjacent = True
    if num[i] > num[i+1]:
      increasing = False
  if (adjacent and increasing):
    candidates.append(number)

print(len(candidates))
for n in range(10):  
  print(candidates[n])
suitables = 0
#throwing out triples+
for number in candidates:
  double = False
  numString = str(number)
  print(numString)
  for k in range(10):
    j = str(k)
    count = 0
    for digit in numString:
      if j == digit:
        print(k)
        print(numString)
        count +=1
    if count == 2:
      double = True
  if double:
    suitables += 1

print(suitables)