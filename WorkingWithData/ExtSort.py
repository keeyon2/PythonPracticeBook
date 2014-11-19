import pdb

def sortByExt(x):
    y = x.split('.')
    return y[1]

# Sorting by Length of list
def extsort(StringList):
    print 'In Function'
    StringList.sort(key = sortByExt)
    print StringList
    return StringList

# give lensort(stringList) and unique/dup(numList)
if __name__ == '__main__':
    stringList = ['python', 'perl', 'java', 'c', 'haskell', 'ruby']
    stringListExt = ['a.c', 'a.py', 'b.py', 'bar.txt', 'foo.txt', 'x.c']
    numList = [1, 2, 3, 4, 3, 4, 1, 2, 5, 6, 2, 3, 1, 23, 5, 1, 3]
