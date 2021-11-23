# get input
# ledger = []
# with open('input.txt') as file:
# for line in file:
# append the text line as an integer
# ledger.append(int(line.strip()))

# print(ledger[:10])

# test = [1721, 979, 366, 299, 675, 1456]


def find2020(numList):
    length = len(numList)
    # find two numbers that add to 2020
    # cycle through all entries
    for i in range(length):
        # cycle through all entries
        for j in range(length):
            # ensure we don't double a signle entry of 1010
            if not i == j:
                a = numList[i]
                b = numList[j]
                # check for 2020
                if a + b == 2020:
                    # multiply them together
                    # return result
                    return a * b


def find2020Again(numList):
    length = len(numList)
    # find two numbers that add to 2020
    # cycle through all entries
    for i in range(length):
        # cycle through all entries
        for j in range(length):
            for k in range(length):
                # ensure we don't double one of the entries
                if not i == j == k:
                    a = numList[i]
                    b = numList[j]
                    c = numList[k]
                    # check for 2020
                    if a + b + c == 2020:
                        # multiply them together
                        # return result
                        return a * b * c


# print(find2020(ledger))

# print(find2020Again(ledger))
