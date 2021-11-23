filename = 'test.txt'
# filename = 'input.txt'
rules={}
puzzleInput = []
strings= []
with open(filename) as file:
  for line in file:
    halves = line.strip().split(':')
    if len(halves) == 2:
      rules[halves[0]] = halves[1].strip()
    elif line != "\n":
      strings.append(line.strip())

print(rules)
print(strings)
# find initial strings
for rule in rules:
  if rules[rule] == '\"a\"' or rules[rule] == '\"b\"':
    rules[rule] = rules[rule].strip("\"")
print(rules)
# recursively build strings
stillChecking = True
for rule in rules:
  rules[rule] = rules[rule].split()
print(rules)

while stillChecking:
  stillChecking = False
  for rule in rules:
    ruleList = rules[rule]
    print(ruleList)
    for i in range(len(ruleList)):
      if ruleList[i] != '|' and ruleList[i] in rules.keys():
        ruleList[i] = ' '.join(rules[ruleList[i]])
        stillChecking = True

print(rules)




#attempt to match string
