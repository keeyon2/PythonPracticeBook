import pdb

# Sorting by Length of list
def lensort(StringList):
    print 'In Function'
    StringList.sort(key = lambda y: len(y))
    print StringList
    return StringList

#  Given list, returns set without using set function  
def unique(List):
    solution = []
    for x in List:
        if List.count(x) is 1:
            solution.append(x)
    return solution

# Given list, returns a set of all elemements that were a
# duplicate in the previous list
def dup(List):
    solution = []
    for x in List:
        if (List.count(x) > 1) and (solution.count(x) is 0):
            solution.append(x)
    return (solution)

# give lensort(stringList) and unique/dup(numList)
if __name__ == '__main__':
    stringList = ['python', 'perl', 'java', 'c', 'haskell', 'ruby']
    numList = [1, 2, 3, 4, 3, 4, 1, 2, 5, 6, 2, 3, 1, 23, 5, 1, 3]
