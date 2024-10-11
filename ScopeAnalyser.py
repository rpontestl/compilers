class IdentifierObject:
    def __init__(self, name):
        self.name = name
        self.next = None

class BlockIndentiferList:
    def __init__(self):
        self.head = None

    def insertIdentifierObject(self, identifierName):
        identifier = IdentifierObject(identifierName)
        if self.head is None:
            self.head = identifier
        else:
            last = self.head
            while last.next is not None:
                last = last.next
            last.next = identifier

currentLevel = -1
blockIdentifierList = []

def createNewBlock():
    blockIdentifierList.append(BlockIndentiferList())
    currentLevel = currentLevel + 1

def endBlock():
    blockIdentifierList.pop()
    currentLevel = currentLevel - 1

def define(identifierName):
    object = IdentifierObject(identifierName)
    blockIdentifierList[currentLevel].insertIdentifierObject(object)

def searchCurrentLevel(identifierName):
    identifierList = blockIdentifierList[currentLevel]
    element = identifierList.head
    while element.next is not None:
        if element.name == identifierName:
            return element
        element = element.next
    return element

def searchAllLevels(identifierName): 
    level = currentLevel
    while level >= 0:
        levelMatch = searchCurrentLevel(identifierName)
        if levelMatch is not None:
            return levelMatch
        level = level - 1
    return None



    
